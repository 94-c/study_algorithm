# id를 key값으로 pw를 value값으로 dict로 만들어서 비교
def solution(id_pw, db):
    db_dict = {i[0]: i[1] for i in db}
    # id 가 있을 때
    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    # id가 없을 때
    else:
        return "fail"