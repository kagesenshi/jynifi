from urlparse import parse_qs


def qs_to_attributes(session, REL_SUCCESS, REL_FAILURE):
    ffl = session.get(100)

    if ffl.isEmpty():
        return

    for ff in ffl:
        qs = ff.getAttribute('http.query.string')
        if qs:
            parsed = parse_qs(qs)

            for k, v in parsed.items():
                session.putAttribute(ff, 'http.GET.%s' % k, v[0])

        session.transfer(ff, REL_SUCCESS)
