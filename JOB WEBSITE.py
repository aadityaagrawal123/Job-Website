headline = print("WELCOME TO OUR WEBSITE, FILL THE DETAILS GIVEN TO APPLY FOR THE JOB               [CEO: Aaditya Agrawal]")
no1 = int(input("Enter your age to apply for the job: "))
if no1 < 18:
    print("                Oh! Your age should be above 17 to apply for the job")
elif no1 < 50 and no1 > 17:
       print("                      ^_^   You are eligible for the job   ^_^")
       name = input("Enter your Name here:")
       birth = int(input("Enter your birth year(YYYY):"))
       if birth < 2004 and birth > 1971:
                               education = int(input("Enter your education level number from these- [1. lower primary /2. secondary stage /3. higher secondary /4. undergraduate /5.  postgraduate /6. Master's /7. doctorate):"))
                               interview = int(input(" available slots for the interview:"
                                                     " 10am-11am / 11am-12pm / 12pm-1pm / 1pm-2pm / 2pm-3pm / 3pm-4pm"
                                                     "        Enter the slot number you want (between 1-6): "))
                               slot = print("Your slot has been confirmed at slot no.", interview)
                               phno = int(input("Enter your phone number (Eg- +91XXXXXXXXXX): "))
                               gotph = print("phone number got successfully")
                               email = input("Enter your email address (eg- xxxxx@gmail.com): ")
                               gotemail = print("email address got successfully")
                               technology = int(input("Select the cateogory to work & enter the option no-[1.technological department/ 2.financial department/ 3.advertising department/ 4.safety department/ 5.cleaning department]:"))
                               username = input("Enter a suitable username for you: ")
                               password = input("Now enter a suitable password for you: ")
                               askusername = input("Now, Enter your username: ")
                               askpassword = input("Now, Also enter your password to get your ID Card: ")
                               correct = print("                       YOUR INFORMATION ON ID CARD WILL BE:")
                               finalname = print("                       NAME: ",name)
                               finalage = print("                       AGE: ",no1)
                               finalsay = print("                       Give this OTP when you go for the interview: 381567")
                               
                               congratulations = print("    Bravo!", name ,"see you in the interview, be on time.... ALL THE BEST" )                            
       elif birth > 2004 or birth < 1971:
                                         print( "Your age is", 2022 - birth,", not", no1," !!!","                          @_@    WARNING: Do not enter wrong information otherwise you will be reported to the cybercrime department" )
       else:
            print("                   Sorry, wrong information")
           
else:
    print("                       Sorry!, you are too old for the job")
    

