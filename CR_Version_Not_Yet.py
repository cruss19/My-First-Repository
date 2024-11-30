# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:43:35 2024

@author: cruss
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:34:44 2024

@author: cruss
"""
print ("This is how it is done")
import os
import shutil

ReportsPath = r'C:\Users\cruss\MyPythonScripts\PythonPractise\Reports'
if not os.path.exists(ReportsPath):
    #os.remove(ReportsPath)
#else:
    os.makedirs (ReportsPath)

AssignmentPath = r'C:\Users\cruss\MyPythonScripts\PythonPractise'
if not os.path.exists(AssignmentPath):
    #shutil.rmtree(AssignmentPath)
#else:
    os.makedirs(AssignmentPath)


os.chdir(AssignmentPath)
os.listdir(AssignmentPath)
os.listdir(ReportsPath)
def Main_Menu():

    while(True):
        # Forever loop. Needs a break, return, or exit() statement to
        # exit the loop.
        # Placing the menu inside of the while loop "Refreshes" the menu
        # if an incorrect value is supplied.
        # Notice the Multiline """ String

        options = None  # Declares a menu variable as empty.

        print("==============================================")

        print("MAIN MENU")
 
        print("From the following three options:")
 
        print("==============================================")
 
        print("1) Enter hours worked")
 
        print("2) Generate employee timesheet reports")
 
        print("3) Exit the Application")
 
        options = input("Enter the number of your menu choice: ")

        # Check what choice was entered and act accordingly
        

        if options == '1' :
            New_Employee_Record()

        if options == '2' :
            View_Reports() 
                   
        if options == '3' :
            Enter_Exit_Application
            
            break
        #else:
            #print("Invalid option. Please enter a number from the Menu Options.")

# ---> END of MAIN MENU <---

def New_Employee_Record():

    import csv
    
    Emp = ["E1", "E2"]

    class GetEmpRecord: 
                     
            
        def __init__ (self, Emp):
            
            
            self.Keys = ['EmpId', "EmpName", "WeekNumber",
                         "Monday","Tuesday", "Wednesday",
                               "Thursday","Friday"]
            
            self.Weekdays = self.Keys[3:]
            
            
            def InputData (self):
                
                Inputs =  []
                            
                print ("Please provide the Employee Details: ")
                EmID = (input ("Employee ID: "))
                EmID = EmID.upper()
                
                Inputs.append (EmID) 
                Inputs.append (input ("Employee Name: "))
                Inputs.append (input ("Week Number: "))
                print ("Enter hours worked for employee " + Inputs[1])
                Inputs.append (input ("Hours worked Monday: "))
                Inputs.append (input ("Hours worked Tuesday: "))
                Inputs.append (input ("Hours worked Wednesday: "))
                Inputs.append (input ("Hours worked Thursday: "))
                Inputs.append (input ("Hours worked Friday: "))                
                return Inputs
            
            self.Inputs = InputData(self)
                        
            def HoursWorked (self):
                Hours = self.Inputs [3:]
                return Hours            
            
            self.HoursWorked = HoursWorked(self)
            
            def EmpDetails (self):                
                Details = self.Inputs[:3]
                return Details            
            
            self.EmpDetails = EmpDetails (self)

            
            def TotalHours (self):                 
                TotalHours = sum(int(x) for x in self.Inputs[3:])
                return (TotalHours)            
            
            self.TotalHours = TotalHours(self)
            
            def FullRecord (self):
                Record = dict(zip(self.Keys, self.Inputs))                
                return Record            
            
            self.FullRecord = FullRecord(self)
            
            def WeeklyReportDict (self):
                WeeklyReportedHours = dict(zip(self.Weekdays, self.HoursWorked))
                return WeeklyReportedHours            
            
            self.WeeklyReportDict = WeeklyReportDict(self)
            
            def WeekNumber (self):
                WeekNumber = self.Inputs[2]
                return str(WeekNumber)            
            
            self.WeekNumber = WeekNumber(self)
     


    for Emp in Emp:
        
        G = GetEmpRecord(Emp)
     
        WH = [G.WeekNumber, str(G.TotalHours)]
        
        ReportFirstline = str('Week: ' + WH[0] +' Total Hours: ' + WH[1])
                
        SummaryFilename = f"{G.Inputs[0]} Week {G.Inputs[2]} Summary.csv"
        #SummaryFilename = str(G.Inputs[0]) + "_Week_"+str(G.Inputs[2]) +".csv"
        
        ReportFilename = f"{G.Inputs[0]} Week {G.Inputs[2]} Report.csv"

              
        
        with open (SummaryFilename, 'w', newline = '') as f:
            
            min_daily_hours = 8
            max_daily_hours = 10
            min_weekly_hours = 30
            max_weekly_hours = 40
            
            lines = []
            
            lines.append ('=======================================' + '\n')
            lines.append ('Summary for Employee: ' + G.EmpDetails[1] + ' ID: ' 
                          + G.EmpDetails [0] + '\n' 
                          + '-------- WEEK: ' + G.EmpDetails[2] + '--------'+'\n')
            
                                         
            for Day, Hours in G.WeeklyReportDict.items():
                
                if int(Hours) < min_daily_hours:
                    
                    lines.append ("Hours worked "  + str(Day) + ': ' + str(Hours) + 
                                  '   Note: This was below minimum hours.' + '\n')
                    
                
                if min_daily_hours <= int(Hours) <= max_daily_hours:
                    lines.append ("Hours worked " + str(Day) +': ' + str(Hours) + '\n')
                
                #elif int(Hours) >=  max_daily_hours:
                    
                 #   print ('that''s bullshit try again')
                else:
                     lines.append ("Hours worked " + str(Day) +': ' + str(Hours) + 
                                   '   Note: This was too many hours.' + '\n')
                     
            f.writelines (lines)
                    
            lines_2 = []   
                
            lines_2.append ('\n' + "Hours worked TOTAL: " + str(G.TotalHours))
            
            if G.TotalHours < min_weekly_hours:
                
                lines_2.append (' Which is BELOW the minimum acceptable number. '+'\n')
                              
            elif min_weekly_hours <= G.TotalHours <= max_weekly_hours:
                
                lines_2.append (' Which was within the ACCEPTABLE range. ' +'\n')
            
            elif G.TotalHours > max_weekly_hours:
                 lines_2.append (' Which is ABOVE the acceptable number. ' +'\n')
            
            ReportSecondline = lines_2
            
            lines_2.append ('----------------END of Reort ----------------------'+'\n')
            
            f.writelines(lines_2)
            
        with open (SummaryFilename, 'r') as reader: 
            print(reader.read())
 
    # End of Summary      NOTE:  I'm printing this as a part of the data entry     
        
            
        with open (ReportFilename, 'w') as f:
            
            f.write ('\n')
            f.writelines (ReportFilename)
            f.writelines ('\n')
            f.writelines (ReportFirstline)
            f.writelines (ReportSecondline)
            
        with open (ReportFilename, 'a',  newline = '') as f: 
            
            w = csv.writer(f, delimiter = ':')         
            w.writerows (G.FullRecord.items())
            
  
        with open (ReportFilename, 'r') as reader:
            print(reader.read())
            
    # Main_Menu()
# New_Employee_Record()

# ---> END of NewEmployeeRecord <---

def View_Reports():
     
    
    def Generate_Reports_Dir ():
        
        for file in os.listdir(AssignmentPath):
        
            if file.endswith('Report.csv'):
                
                old_file = f"C:/Users/cruss/MyPythonScripts/PythonPractise/{file}"
                new_file = f"C:/Users/cruss/MyPythonScripts/PythonPractise/Reports/{file}"
                os.rename (old_file, new_file)
    
    Reports_Dir = Generate_Reports_Dir ()
    
    def Get_List_Sorted ():
        
        
        ListToSort = []
            
        for file in os.listdir(ReportsPath):
                
            def MakeList (file):
                
                key = file.split()[2]
                
                ID = file.split()[0]
                
                if len(key) < 2:
                    key = f"0{key}"
                    
                else:
                    key = f"{key}"
                        
                return (key, ID, file)
                
            ListFile = MakeList(file)
            
            ListToSort.append (ListFile)
            
        ListSorted = sorted(ListToSort, key = lambda data: data[0], reverse=True)
        
        return ListSorted
        
    ListSorted = Get_List_Sorted()
    #print (ListSorted)
    
    #for item in ListSorted:
    #    print (f"{item}'\n'")
    
    def Generate_Report ():
        
        def Report_Option ():
            
            os.chdir(ReportsPath)
            
            ReportOption = int(input ("Enter '1' for reports list by staff ID, OR \n"
                                     "Enter '2' for a list of x reports (most recent first): "))
            
            
            #ReportsToShow = input ("How many reports would you like to generate?: ")
            return (ReportOption)
                
        ReportOption = Report_Option()
        
        if ReportOption == 2:
            
            ReportsToShow = input ("Enter the number of reports to generate, OR \n"
                                       "tye 'all' to generate all emloyee records?: ")
        
            #ReportsToShow = int(input ("Enter the number of reports to generate, OR \n"
                                #       "tye all to dislay all emloyee records?: "))
    #i = int(ReportsToShow)
            
            if ReportsToShow.isdigit():
                
                Reports_List = ListSorted [:int(ReportsToShow)]
                #print (Reports_List)
# this next block essentially accets any nondigit inut as being 'all'
# can use secificatoifor all and error handling
                
            elif ReportsToShow.upper() == 'ALL':
                Reports_List = ListSorted
            
            for Report in Reports_List:
            
                f = Report[2]
                with open (f, 'r') as f:
                
                    print(f.read())
                
        if ReportOption == 1:
            
            IDsToShow = input ("Enter a Staff ID to view all their reports: ")
            IDsToShow = IDsToShow.upper()
            
            List =[]
            for report in ListSorted:
               if report[1] == IDsToShow:
                   #print (report)
                   List.append (report)
            #print (List) 
            for report in List:
                
                f = report[2]
                with open (f, 'r') as f:
                    
                    print (f.read())
                    
            
    Report = Generate_Report()      

#  ======================================================================
Main_Menu()
