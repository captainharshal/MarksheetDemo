from MarksheetDAO import MarksheetDAO
from MarksheetBean import MarksheetBean


class TestMarksheetDAO:

    @staticmethod
    def testAdd():
        model = MarksheetDAO()
        bean = MarksheetBean()

        bean.rollNo = bean.nextrn()
        bean.studentName = input("Enter Student Name:\n")
        bean.physicsScore = input("Enter Physics Score:\n")
        bean.chemistryScore = input("Enter chemitry Score:\n")
        bean.mathsScore = input("Enter Maths Score:\n")

        row_Affected = model.addMarksheet(bean)

        if (row_Affected > 0):
            print("{} row affected".format(row_Affected))
        else:
            print("Zero row affected")

    @staticmethod
    def testGet():
        model = MarksheetDAO()

        rn = input("Enter Roll No:\n")

        marksheet = model.getMarksheet(rn)

        if marksheet is None:
            print("Roll No. does not exist. Please enter the correct roll no.")
        else:
            print("------Marksheet Info------")
            print("Roll No:", marksheet.rollNo)
            print("Student Name:", marksheet.studentName)
            print("Physics Score:", marksheet.physicsScore)
            print("Chemistry Score:", marksheet.chemistryScore)
            print("Maths Score:", marksheet.mathsScore)

    @staticmethod
    def testDelete():
        model = MarksheetDAO()

        rn = input("Enter Roll No:\n")

        record_Affected = model.deleteMarksheet(rn)

        if record_Affected == 0:
            print("Roll No. does not exist. Please enter the correct roll no.")
        elif record_Affected == 1:
            print("Record Deleted Successfully.")

    @staticmethod
    def testUpdate():
        model = MarksheetDAO()

        rn = input("Enter Roll No:\n")

        record_Affected = model.updateMarksheet(rn)

        if record_Affected == 0:
            print("Roll No. does not exist. Please enter the correct roll no.")
        elif record_Affected == 1:
            print("Record Updated Successfully.")

    @staticmethod
    def testMeritlist():
        model = MarksheetDAO()

        meritList = model.MeritlistMarksheet()

        print("-----------------------------------------------------------------------------")
        print("Roll No. ||\tStudent Name ||\tPhysics ||\tChemistry ||  Maths ||\t Total Score")
        print("-----------------------------------------------------------------------------")
        for row in meritList:
            print("\t{}\t\t{}\t\t\t  {}\t\t\t{}\t\t\t{}\t\t\t{}".format(row[1], row[2], row[3], row[4], row[5], row[6]))

    @staticmethod
    def testSearch():
        model = MarksheetDAO()
        bean = MarksheetBean()

        bean.rollNo = input("Enter Roll No:\n")
        bean.studentName = input("Enter Student Name:\n")
        bean.physicsScore = input("Enter Physics Score:\n")
        bean.chemistryScore = input("Enter chemitry Score:\n")
        bean.mathsScore = input("Enter Maths Score:\n")

        searchList = model.searchMarksheet(bean)

        if searchList is None:
            print("Record does not Match. Please enter the correct details.")
        else:
            print("-----------------------------------------------------------------------------")
            print("Roll No. ||\tStudent Name ||\tPhysics ||\tChemistry ||  Maths ||\t Total Score")
            print("-----------------------------------------------------------------------------")
            for row in searchList:
                print("\t{}\t\t{}\t\t\t  {}\t\t\t{}\t\t\t{}\t\t\t{}".format(row[1], row[2], row[3], row[4], row[5],
                                                                            row[6]))

    def testMarksheet(self):
        print("Enter the option:")
        option = input(
            "1 to Add Record OR 2 to Get Record OR 3 to Delete Record OR 4 to Update Record OR 5 to Search Marksheet "
            "OR 6 to Generate Merit List\n")

        if option == '1':
            TestMarksheetDAO.testAdd()
        elif option == '2':
            TestMarksheetDAO.testGet()
        elif option == '3':
            TestMarksheetDAO.testDelete()
        elif option == '4':
            TestMarksheetDAO.testUpdate()
        elif option == '5':
            TestMarksheetDAO.testSearch()
        elif option == '6':
            TestMarksheetDAO.testMeritlist()
        else:
            print("Please Enter the Correct Option.")


if __name__ == "__main__":
    testMarksheet = TestMarksheetDAO()
    testMarksheet.testMarksheet()
