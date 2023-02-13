import DatabaseConn as DbConn
from MarksheetBean import MarksheetBean


class MarksheetDAO:

    def addMarksheet(self, bean=None):

        if isinstance(bean, MarksheetBean):
            conn = DbConn.getConnection("marksheetdb1")
            csr = conn.cursor()

        rn = bean.rollNo
        name = bean.studentName
        ph_score = bean.physicsScore
        ch_score = bean.chemistryScore
        mth_score = bean.mathsScore

        conn = DbConn.getConnection("marksheetdb1")
        csr = conn.cursor()
        inst_qry = "INSERT INTO marksheet2 (roll_no,student_name,physics_score,chemistry_score,maths_score) values (" \
                   "%s,%s,%s,%s,%s) "
        row = csr.execute(inst_qry, (rn, name, ph_score, ch_score, mth_score))
        conn.commit()
        csr.close()
        conn.close()

        if (row > 0):
            return 1
        else:
            return 0

    def getMarksheet(self, rollNo=0):

        conn = DbConn.getConnection("marksheetdb1")
        csr = conn.cursor()
        slt_qry = "SELECT roll_no from marksheet2 where roll_no=%s"
        row = csr.execute(slt_qry, (rollNo,))
        csr.close()
        conn.close()

        if row == 0:
            return None
        else:
            conn = DbConn.getConnection("marksheetdb1")
            csr = conn.cursor()
            slt_qry = "SELECT * from marksheet2 where roll_no=%s"
            csr.execute(slt_qry, (rollNo,))
            result = csr.fetchone()
            csr.close()
            conn.close()
            marksheet = MarksheetBean()
            marksheet.rollNo = result[1]
            marksheet.studentName = result[2]
            marksheet.physicsScore = result[3]
            marksheet.chemistryScore = result[4]
            marksheet.mathsScore = result[5]
            return marksheet

    def deleteMarksheet(self, rollNo=0):

        conn = DbConn.getConnection("marksheetdb1")
        csr = conn.cursor()
        slt_qry = "SELECT roll_no from marksheet2 where roll_no=%s"
        row = csr.execute(slt_qry, (rollNo,))
        csr.close()
        conn.close()

        if row == 0:
            return 0
        else:
            conn = DbConn.getConnection("marksheetdb1")
            csr = conn.cursor()
            del_qry = "DELETE from marksheet2 where roll_no=%s"
            csr.execute(del_qry, (rollNo,))
            conn.commit()
            csr.close()
            conn.close()
            return 1

    def updateMarksheet(self, rollNo=0):

        conn = DbConn.getConnection("marksheetdb1")
        csr = conn.cursor()
        slt_qry = "SELECT roll_no from marksheet2 where roll_no=%s"
        row = csr.execute(slt_qry, (rollNo,))
        csr.close()
        conn.close()

        if row == 0:
            return 0
        else:
            conn = DbConn.getConnection("marksheetdb1")
            csr = conn.cursor()
            nm = input("Enter New Name:\n")
            ph_score = input("Enter New Physics Score:\n")
            ch_score = input("Enter New chemitry Score:\n")
            mth_score = input("Enter New Maths Score:\n")
            upd_qry = "UPDATE marksheet2 set student_name=%s,physics_score=%s,chemistry_score=%s,maths_score=%s where " \
                      "roll_no=%s "
            csr.execute(upd_qry, (nm, ph_score, ch_score, mth_score, rollNo))
            conn.commit()
            csr.close()
            conn.close()
            return 1

    def searchMarksheet(self, bean=None):

        if isinstance(bean, MarksheetBean):
            conn = DbConn.getConnection("marksheetdb1")
            csr = conn.cursor()

            rn = bean.rollNo
            name = bean.studentName
            ph_score = bean.physicsScore
            ch_score = bean.chemistryScore
            mth_score = bean.mathsScore

            slt_qry = "SELECT *, (physics_score+chemistry_score+maths_score) as TOTAL_SCORE from marksheet2 WHERE " \
                      "roll_no=%s OR student_name=%s OR physics_score=%s OR chemistry_score=%s OR maths_score=%s "

            row = csr.execute(slt_qry, (rn, name, ph_score, ch_score, mth_score))

            if row == 0:
                return None
            else:
                Result = csr.fetchall()
                return Result

            csr.close()
            conn.close()

    def MeritlistMarksheet(self):

        conn = DbConn.getConnection("marksheetdb1")
        csr = conn.cursor()
        slt_qry = "SELECT *, (physics_score+chemistry_score+maths_score) as TOTAL_SCORE from marksheet2 order by " \
                  "TOTAL_SCORE desc "

        csr.execute(slt_qry)

        Result = csr.fetchall()
        return Result

        csr.close()
        conn.close()
