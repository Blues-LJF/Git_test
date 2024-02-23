def dsgz(jbgz):
    if jbgz < 5000:
        jbgz = jbgz
    elif jbgz >= 5000 and jbgz < 10000:
        jbgz = jbgz - jbgz * 0.05
    else:
        jbgz = jbgz - jbgz * 0.1
    print(jbgz)


def jixiao(jbgz):
    if jbgz >= 10000:
        jbgz = jbgz + 2000
    else:
        jbgz = jbgz + 1000


def main():
    ds = dsgz(5000)
    jx = jixiao(ds)
    print(ds + jx)


if __name__ == "__main__":
    print(__name__)
    main()
