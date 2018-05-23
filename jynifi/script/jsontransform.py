# JSON Transformation DSL for NiFi
#
# Variables:
#
# * transformRule
# * outputSkeleton
#

import json
import copy
import yaml
import imp
import os
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from rulez.transformer import Engine


class JSONDecodeError(Exception):
    pass


class TransformCallback(StreamCallback):

    def __init__(self, engine, rule, dest):
        self.engine = engine
        self.rule = rule
        self.dest = copy.deepcopy(dest)

    def process(self, inputStream, outputStream):
        try:
            src = json.loads(IOUtils.toString(
                inputStream, StandardCharsets.UTF_8))
        except ValueError, e:
            raise JSONDecodeError()
        dest = self.engine.remap(self.rule, src, self.dest)
        outputStream.write(bytearray(json.dumps(dest)))


def jsontransform(session, REL_SUCCESS, REL_FAILURE, transformRule,
                  outputSkeleton, extensionModules):

    ffl = session.get(100)

    if ffl.isEmpty():
        return

    for ff in ffl:
    
        mods = []
        for m in extensionModules.getValue().split(','):
            n = os.path.basename(m)[:-2]
            mods.append(imp.load_source(n, m))
    
        if not Engine.is_committed():
            Engine.commit()
    
        rule = yaml.load(transformRule.evaluateAttributeExpressions(ff).getValue())
        skel = outputSkeleton.getValue()
        if skel.startswith('file://'):
            dest = json.loads(open(skel[7:]).read())
        else:
            dest = json.loads(skel)
    
        tc = TransformCallback(Engine(), rule, dest)
    
        try:
            session.write(ff, tc)
        except JSONDecodeError, e:
            session.transfer(ff, REL_FAILURE)
            return
        session.transfer(ff, REL_SUCCESS)
