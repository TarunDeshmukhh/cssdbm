                                ----Staff & Students Database Management App----
								
								
Note - This app is only for management commitee person , Thats why there is no registration form for login 
       There will be only 1-2 user for this app beacause the information will be confidential while will used.
       However can add the registration form on Home if required .	   
	   
1.home.html - 
              College Name Heading 
			  Login -
			         Username
					 Password
					 Submit    
			  Redirect : submit to dashboard

2.dashboard.html -
			  Teaching Staff
			  Non-Teaching Staff
			  Students Info 
			  Logout
			  Redirect : to teachinglist/nontechinglist/studentlist
			             logout to home
			  
3.teachinglist.html -
              Teaching Staff -
			  Name - View 	
			  New Registraion
			  Back
			  logout
			  Redirect : view to teachingstaff
			             new registration to newregistraion 
			             logout to home
			             back to dashboard
			  
              			  
4.nonteachinglist.html - 
              Non-Teaching Staff -
			  Name - View 
              New Registraion			  
			  Back
			  logout
			  Redirect : view to nonteachingstaff
			             new registration to newregistraion
			             logout to home
			             back to dashboard
						 
			  
5.studentlist.html -
              Students -
			  Search by first/middle/last name - Submit
			  Name - Branch - Semester - Year - View 	
			  New Registraion
			  Back
			  logout
			  Redirect : searchsubmit to searchstudent
			             view to studentsinfo
						 new registration to newregistraion
			             logout to home
			             back to dashboard
	
			  
6.teachingstaff.html -
              1.Name
			  2.Age / Gender
			  3.Address
			  4.Education
			  5.Subjects Expertise 
			  6.Job Position
			  7.Aadhar number
			  8.Pan number
			  9.Salary Account Details
			 10.Salary
			 11.Back
			 12.logout
			 13.Edit
			 14.Delete
			 redirect : logout to home
			            back to teachinglist
						edit to registrationteach
						delete to teachinglist
			 
			
			  
7.nonteachingstaff.html -
              1.Name
			  2.Age / Gender
			  3.Address
			  4.Education
			  5.Job Position
			  6.Aadhar number
			  7.Pan number
			  8.Salary Account Details
			  9.Salary
			 10.Back
			 11.logout
			 12.Edit
			 13.Delete
			 redirect : logout to home
			            back to nontechinglist
						edit to registrationnonteach
						delete to nonteachinglist
			 
8.studentsinfo.html -
              1.Name
			  2.Age
			  3.Gender
			  4.Caste
			  5.Current Semester			  
			  6.Current Year
			  7.Branch
			  8.Education 
			  9.Aadhar number
			 10.Address
			 11.Back
			 12.logout
			 13.Edit
			 14.Delete
			 redirect : logout to home
			            back to studentlist
						edit to registrationstudent
						delete to studentlist
			 
9.newregistraion.html -
              position - 
			               Student --> Submit
						   Teaching Staff --> Submit
						   Non-Teaching Staff --> Submit
						   logout
						   Back
			  redirect :logout to home
			            back to dashboard
						submit to registrationstudent
						submit to registrationteach
						submit to registrationnonteach
						
10.registrationteach.html -
              1.Name
			  2.Age / Gender
			  3.Address
			  4.Education
			  5.Subjects Expertise 
			  6.Job Position
			  7.Aadhar number
			  8.Pan number
			  9.Salary Account Details
			 10.Salary
			 11.Submit
			 12.Back
			 13.logout
			 redirect : logout to dashboard
			            submit to teachinglist
						back to newregistraion

11.registrationnonteach.html - 
              1.Name
			  2.Age / Gender
			  3.Address
			  4.Education
			  5.Subjects Expertise 
			  6.Job Position
			  7.Aadhar number
			  8.Pan number
			  9.Salary Account Details
			 10.Salary
			 11.Submit
			 12.Back
			 13.logout
			 redirect : logout to dashboard
			            submit to nonteachinglist
						back to newregistraion
						
12.registrationstudent.html -						  
              1.Name
			  2.Age
			  3.Gender
			  4.Caste
			  5.Current Semester			  
			  6.Current Year
			  7.Branch
			  8.Education 
			  9.Aadhar number
			 10.Address
			 11.Submit
			 12.Back
			 13.logout
			 redirect : logout to dashboard
			            submit to studentlist
						back to newregistraion

13.searchstudent.html -
              Students
			  Name - Branch - Semester - Year - View 
			  Back
			  logout
			  redirect :view to studentsinfo
			            logout to home
						back to studentlist
			 	
			 
              
			 
			 


          
			  

			  
		
              