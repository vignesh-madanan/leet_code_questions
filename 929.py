# 929. Unique Email Addresses
# everything after + is ignored
# txt.as@gmail.com is interpreted as txtas#@gmail.com


def solution(emails):
    results = []
    for email in emails:
        _split = email.split("@")
        subdomain = _split.pop()
        local_name = _split.pop()

        # replace . with
        local_name = local_name.split("+")

        local_name = local_name.replace(".", "")

        local_name.pop()
        final_name = local_name.pop() + "@" + subdomain
        results.append(final_name)

    return len(set(results))


if __name__ == "__main__":
    print(
        list(
            map(
                solution,
                [
                    [
                        "fg.r.u.uzj+o.pw@kziczvh.com",
                        "r.cyo.g+d.h+b.ja@tgsg.z.com",
                        "fg.r.u.uzj+o.f.d@kziczvh.com",
                        "r.cyo.g+ng.r.iq@tgsg.z.com",
                        "fg.r.u.uzj+lp.k@kziczvh.com",
                        "r.cyo.g+n.h.e+n.g@tgsg.z.com",
                        "fg.r.u.uzj+k+p.j@kziczvh.com",
                        "fg.r.u.uzj+w.y+b@kziczvh.com",
                        "r.cyo.g+x+d.c+f.t@tgsg.z.com",
                        "r.cyo.g+x+t.y.l.i@tgsg.z.com",
                        "r.cyo.g+brxxi@tgsg.z.com",
                        "r.cyo.g+z+dr.k.u@tgsg.z.com",
                        "r.cyo.g+d+l.c.n+g@tgsg.z.com",
                        "fg.r.u.uzj+vq.o@kziczvh.com",
                        "fg.r.u.uzj+uzq@kziczvh.com",
                        "fg.r.u.uzj+mvz@kziczvh.com",
                        "fg.r.u.uzj+taj@kziczvh.com",
                        "fg.r.u.uzj+fek@kziczvh.com",
                    ]
                ],
            )
        )
    )
