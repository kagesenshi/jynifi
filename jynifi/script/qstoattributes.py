from urlparse import parse_qs


def qs_to_attributes(session, REL_SUCCESS, REL_FAILURE):
    ff = session.get()

    if ff is not None:
        qs = ff.getAttribute('http.query.string')
        if qs:
            parsed = parse_qs(qs)

            for k, v in parsed.items():
                session.putAttribute(ff, 'http.GET.%s' % k, v[0])

        session.transfer(ff, REL_SUCCESS)
