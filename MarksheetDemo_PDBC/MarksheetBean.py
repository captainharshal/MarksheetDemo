import DatabaseConn as DbConn

class MarksheetBean:

    def __init__(self) -> None:
        self.__rNo = 0
        self.__stdName = None
        self.__phyScore = 0
        self.__chemScore = 0
        self.__mthScore = 0


    # function to get value of Roll No.
    def __getRollno(self):
        return self.__rNo

    # function to set value of Roll No.
    def __setRollno(self, rn):
        self.__rNo = rn

    # use of property() function
    rollNo = property(__getRollno, __setRollno)


    # function to get value of Student Name
    def __getStudentname(self):
        return self.__stdName

    # function to set value of Student Name
    def __setStudentname(self, nm):
        self.__stdName = nm

    # use of property() function
    studentName = property(__getStudentname, __setStudentname)


    # using property decorator
    # a getter function for Physics Score
    @property
    def physicsScore(self):
        return self.__phyScore

    # a setter function for Physics Score
    @physicsScore.setter
    def physicsScore(self, phy):
        self.__phyScore = phy


    # using property decorator
    # a getter function for Chemistry Score
    @property
    def chemistryScore(self):
        return self.__chemScore

    # a setter function for Chemistry Score
    @chemistryScore.setter
    def chemistryScore(self, chem):
        self.__chemScore = chem


    # using property decorator
    # a getter function for Maths Score
    @property
    def mathsScore(self):
        return self.__mthScore
       
    # a setter function for Maths Score
    @mathsScore.setter
    def mathsScore(self, mth):
        self.__mthScore = mth

    
    # function to get value of Next Roll Number
    @staticmethod
    def nextrn():

        Roll_No = 0

        conn = DbConn.getConnection("marksheetdb1")
        csr = conn.cursor()

        slt_qry = "select max(roll_no) from marksheet2"

        csr.execute(slt_qry)
        Roll_No = csr.fetchone()
        
        csr.close()
        conn.close()

        if Roll_No[0] is None:
            new_rn = list(Roll_No)
            new_rn[0] = 0
            Roll_No = tuple(new_rn)
        return Roll_No[0] + 1