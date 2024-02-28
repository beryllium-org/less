for pv[get_pid()]["f"] in [
    "less.lja",
    "less.py",
]:
    be.based.run("cp " + vr("f") + " /bin/" + vr("f"))
be.api.setvar("return", "0")
