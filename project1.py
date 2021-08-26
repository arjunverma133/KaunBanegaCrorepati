introduction = " 'KBC': Kaun Banega Crorepati "
introduction1 = " Aapka 'KBC' pe 'SAWAGAT' hai , chaliye 'GAME' shuru karte hai "
introduction2 = " Please ENTER Your GOOD NAME  "

#Rules
dlg01 = "is 'GAME' ko khelne ke 'NIYAM' apke 'COMPUTER SCREEN' par ye rahe"
dlg02 = "aapko dene honge kuch '16' 'SAWAALO' ke sahi 'UTTAR'"
dlg03 = "to, 'KYA AAP TAYAR HAI'"
dlg04 = "agar 'HAA!'to 'ENTER'dabaye"
dlg05 = "aapke 'COMPUTER SCREEN' par pesh hai diye gae sawaalo ki sahi 'RAKAM'"
dlg06 = "aur, sabse 'JAROORI' baat to batana ham bhool hi gae"
dlg07 = "aapke paas hongi kuch lifelines"
dlg08 = "'50-50','EXPERT ADVICE'"
dlg09 = "jo aap 'SAHI TIME' aane par 'ISTEMAAL' kar skte hai"
dlg10 = "apko kya lagta aap  yha se kitni RAKAM le jaenge??"
dlg11 = "ham to yahi 'DUA' karte hai ki aap yahase"
dlg12 = "to jaroor hi lekar jae"
dlg13 = "to chaliye shuru karte hai"

#Questions & Money
rule01 = "Q1=$1,000\nQ2=$2,000\nQ3=$3,000\nQ4=$5,000"
rule02 = "Q5=$10,000\nQ6=$20,000\nQ7=$40,000\nQ8=$80,000"
rule03 = "Q9=$1,60,000\nQ10=$ 3,20,000\nQ11=$6,40,000\nQ12=$12,50,000"
rule04 = "Q13=$25,00,000\nQ14=$50,00,000\nQ15=$1,00,00,000\nQ16=$5,00,00,000"

#----------------------------------------PRINTIMG-----------------------------------------#

print("{0:$>60}{1:$<24}\n\n{2:≈>75}{3:≈<9}\n\n{4:◊>55}{5:◊<29}".format(introduction,"",introduction1,"",introduction2,""))
name = input()
print("{0}!!{1}\n{2}\n{3}".format("hello",name,"nice to meet you","Myself:Amitabh Bacchan"))
print("{0}\n{1}\n{2}\n{3}".format(dlg01,dlg02,dlg03,dlg04))
opinion = input()
print("{0}\n{1}\n{2}\n{3}\n{4}\n\n{5}".format(dlg05,rule01,rule02,rule03,rule04,dlg10))
money = input()
print("{0} {1} {2}\n{3},{4}".format(dlg11,money,dlg12,dlg13,introduction))

input("please press 'ENTER' to start")

#--------------------------------------GAME----START--------------------------------------#

print("to '1 SAWAAL',poore'$1,000'ke liye,apke saamne yeh raha\n")
print("Which among the following is called first, automatically, whenever an object is created")
print("opt1)Constructor                            opt2)Class")
print("opt3)New                                    opt4)Trigger")

ans = input("enter yr ans: ").strip().lower()

if ans == "1" or ans == "a":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("Constructors are the member functions")
    print("which are called automatically whenever an object is created")
    print("It is a mandatory functions to be called for an object to be created")
    print("as this helps in initializing the object to a legal initial value for the class.")
    print("thus,i will prefer you to go with option 1 i.e. 'Constructor'")
    
    
    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "1" or ans == "a":
        print("yes")

    elif ans == "50-50":
        print("opt1)Constructor                            opt2)")
        print("opt3)New                                    opt4)")
        
        ans = input("now plz enter your ans")

        if ans == "1" or ans =="a":
            print("yes")
    
elif ans == "50-50":
    print("opt1)Constructor         opt2)")
    print("opt3)New                 opt4)")
    
    ans = input("now plz enter your ans")

    if ans == "1" or ans =="a":
        print("yes")
        
    elif ans == "EXPERT ADVICE":
        print("Constructors are the member functions")
        print("which are called automatically whenever an object is created")
        print("It is a mandatory functions to be called for an object to be created")
        print("as this helps in initializing the object to a legal initial value for the class.")
        print("thus,i will prefer you to go with option 1 i.e. 'Constructor'")
        

        if ans == "1" or ans =="a":
            print("yes")
        
else:
    print("no")
    exit()
input("press enter!!")

#-------------------------------------------------------------------------------------------#

print("to '2 SAWAAL',poore'$2,000'ke liye,apke saamne yeh raha\n")
print("In which access should a constructor be defined, so that object of the class can be created in any function?")
print("opt1)Private                                        opt2)Protected")
print("opt3)Any access specifier will work                 opt4)Public")

ans = input("enter yr ans: ").strip().lower()

if ans == "4" or ans == "d":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("Constructor function should be available to all the parts of program")
    print("where the object is to be created")
    print("Hence it is advised to define it in public access")
    print("so that any other function is able to create objects")
    print("thus,i will prefer you to go with option 4 i.e. 'Public'")
    
    
    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "4" or ans =="d":
        print("yes")

    elif ans == "50-50":
        print("opt1)Private        opt2)" )
        print("opt3)               opt4)Public")
        ans = input("now plz enter your ans")

        if ans == "4" or ans =="d":
            print("yes")
    
elif ans == "50-50":
    print("opt1)Private        opt2)" )
    print("opt3)               opt4)Public")
    
    ans = input("now plz enter your ans")

    if ans == "4" or ans =="d":
        print("yes")
        
    elif ans == "EXPERT ADVICE":
        print("Constructor function should be available to all the parts of program")
        print("where the object is to be created")
        print("Hence it is advised to define it in public access")
        print("so that any other function is able to create objects")
        print("thus,i will prefer you to go with option 4 i.e. 'Public'")
    
        if ans == "4" or ans =="d":
            print("yes")
        
else:
    print("no")
    exit()
input("press enter!!")    
#-------------------------------------------------------------------------------------------#

print("to '3 SAWAAL',poore'$3,000'ke liye,apke saamne yeh raha\n")
print("Find the maximum sub-array sum for the following array:'{3, 6, 7, 9, 3, 8}'")
print("opt1)32                                          opt2)33")
print("opt3)34                                          opt4)36")

ans = input("enter yr ans: ").strip().lower()

if ans == "4" or ans == "d":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("All the elements of the array are positive")
    print("So, the maximum sub-array sum is equal to the sum of all the elements, which is 36.")
    print("thus,i will prefer you to go with option 4 i.e. '36'")

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "4" or ans =="d":
        print("yes")

    elif ans == "50-50":
        print("opt1)             opt2)"    )
        print("opt3)34         opt4)36")
        
        ans = input("now plz enter your ans")

        if ans == "4" or ans =="d":
            print("yes")
    
elif ans == "50-50":
    print("opt1)             opt2)"    )
    print("opt3)34         opt4)36")
    
    ans = input("now plz enter your ans")

    if ans == "4" or ans =="d":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("All the elements of the array are positive")
        print("So, the maximum sub-array sum is equal to the sum of all the elements, which is 36.")
        print("thus,i will prefer you to go with option 4 i.e. '36'")

        if ans == "4" or ans =="d":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '4 SAWAAL',poore'$5,000'ke liye, apke saamne yeh raha\n")
print("What is the average case running time of an insertion sort algorithm ")
print("opt1)O(N2)                                             opt2)O(N)")
print("opt3)O(N log N)                                        opt4)O(log N)")

ans = input("enter yr ans: ").strip().lower()

if ans == "1" or ans == "A":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("The average case analysis of a tight bound algorithm is mathematically achieved to be O(N2)")
    print("thus,i will prefer you to go with option 1 i.e. 'O(N2)'")
    

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "1" or ans == "a":
        print("yes")

    elif ans == "50-50":
        print("opt1)O(N2)         opt2)O(N)")
        print("opt3)              opt4)")
        
        ans = input("now plz enter your ans")

        if ans == "1" or ans =="a":
            print("yes")
    
elif ans == "50-50":
    print("opt1)O(N2)         opt2)O(N)")
    print("opt3)              opt4)")
    
    ans = input("now plz enter your ans")

    if ans == "1" or ans == "a":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("The average case analysis of a tight bound algorithm is mathematically achieved to be O(N2)")
        print("thus,i will prefer you to go with option 1 i.e. 'O(N2)'")
        if ans == "1" or ans == "a":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")    
#-------------------------------------------------------------------------------------------#
print("to '5 SAWAAL',poore'$10,000'ke liye, apke saamne yeh raha\n")
print("In C, what are the basic loops required to perform an insertion sort?")
print("opt1)do- while                                      opt2)if else")
print("opt3)for and if                                     opt4)for and while")

ans = input("enter yr ans: ").strip().lower()

if ans == "4" or ans == "d":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print(" To perform an insertion sort, we use two basic loops- an outer for loop and an inner while loop")
    print("thus,i will prefer you to go with option 4 i.e. 'for and while'")

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "4" or ans == "d":
        print("yes")

    elif ans == "50-50":
        print("opt1)         opt2)if else")
        print("opt3)         opt4)for and while")
        
        ans = input("now plz enter your ans")

        if ans == "4" or ans =="d":
            print("yes")
    
elif ans == "50-50":
    print("opt1)         opt2)if else")
    print("opt3)         opt4)for and while")
    
    ans = input("now plz enter your ans")

    if ans == "4" or ans =="d":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print(" To perform an insertion sort, we use two basic loops- an outer for loop and an inner while loop")
        print("thus,i will prefer you to go with option 4 i.e. 'for and while'")


        if ans == "4" or ans =="d":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")    
#-------------------------------------------------------------------------------------------#
print("to '6 SAWAAL',poore'$20,000'ke liye, apke saamne yeh raha\n")
print(" If a function has to be called only by using other member functions of the class, what should be the access specifier used for that function?")
print("opt1)Protected                                     opt2)Public")
print("opt3)Private                                       opt4)Default")

ans = input("enter yr ans: ").strip().lower()

if ans == "3" or ans == "c":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("The function should be made private")
    print("In this way, the function will be available to be called only from the class member functions.") 
    print("Hence the function will be secure from the outside world")
    print("thus,i will prefer you to go with option 3 i.e. 'Private'")

    

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "3" or ans == "c":
        print("yes")

    elif ans == "50-50":
        print("opt1)                opt2)Public")
        print("opt3)Private         opt4)")
        
        ans = input("now plz enter your ans")

        if ans == "3" or ans =="c":
            print("yes")
    
elif ans == "50-50":
    print("opt1)                opt2)Public")
    print("opt3)Private         opt4)")
    
    ans = input("now plz enter your ans")

    if ans == "3" or ans =="c":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("The function should be made private")
        print("In this way, the function will be available to be called only from the class member functions.") 
        print("Hence the function will be secure from the outside world")
        print("thus,i will prefer you to go with option 3 i.e. 'Private'")

        if ans == "3" or ans =="c":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '7 SAWAAL',poore'$40,000'ke liye, apke saamne yeh raha\n")
print("Which access specifier is/are most secure during inheritance?")
print("opt1)Default                                        opt2)Private")
print("opt3)Protected                                      opt4)Private and Default")

ans = input("enter yr ans: ").strip().lower()

if ans == "2" or ans == "b":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("The private members are most secure in inheritance")
    print("The default members can still be in inherited in special cases")
    print("but the private members can’t be accessed in any case")
    print("thus,i will prefer you to go with option 2 i.e. 'Private'") 

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "2" or ans == "b":
        print("yes")

    elif ans == "50-50":
        print("opt1)Default         opt2)Private")
        print("opt3)                opt4)")
        
        ans = input("now plz enter your ans")

        if ans == "2" or ans =="b":
            print("yes")
    
elif ans == "50-50":
    print("opt1)Default         opt2)Private")
    print("opt3)                opt4)")
    
    ans = input("now plz enter your ans")

    if ans == "2" or ans =="b":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("The private members are most secure in inheritance")
        print("The default members can still be in inherited in special cases")
        print("but the private members can’t be accessed in any case")
        print("thus,i will prefer you to go with option 2 i.e. 'Private'") 

        if ans == "2" or ans =="b":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '8 SAWAAL',poore'$80,000'ke liye, apke saamne yeh raha\n")
print("Which among the following is true?")
print("opt1)Private member function can’t be overridden    opt2)Private member functions can’t be overloaded")
print("opt3)Private member functions can be overridden     opt4)Private member functions can’t be overloaded with a public member")

ans = input("enter yr ans: ").strip().lower()

if ans == "1" or ans == "a":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("The private member functions can be overloaded but they can’t be overridden")
    print("This is because, overriding means a function with same name in derived class,")
    print("gets more priority when called from object of derived class")
    print("Here, the member function is private so there is no way that it can be overridden.")
    print("thus,i will prefer you to go with option 1 i.e. 'Private member function can’t be overridden '") 


    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "1" or ans == "a":
        print("yes")

    elif ans == "50-50":
        print("opt1)         opt2)")
        print("opt3)ICELAND           opt4)")
        
        ans = input("now plz enter your ans")

        if ans == "1" or ans =="a":
            print("yes")
    
elif ans == "50-50":
    print("opt1)Private member function can’t be overridden         opt2)")
    print("opt3)Private member functions can be overridden          opt4)")
    
    ans = input("now plz enter your ans")

    if ans == "1" or ans =="a":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("The private member functions can be overloaded but they can’t be overridden")
        print("This is because, overriding means a function with same name in derived class,")
        print("gets more priority when called from object of derived class")
        print("Here, the member function is private so there is no way that it can be overridden.")
        print("thus,i will prefer you to go with option 1 i.e. 'Private member function can’t be overridden '") 
        

        if ans == "1" or ans =="a":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '9 SAWAAL',poore'$1,60,000'ke liye, apke saamne yeh raha\n")
print("Which among the following is correct?")
print("opt1)Private specifier must be used before public specifier  opt2) Private specifier must be used before protected specifier")
print("opt3)Private specifier can be used anywhere in class         opt4) Private specifier must be used first")

ans = input("enter yr ans: ").strip().lower()

if ans == "3" or ans == "c":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("The private specifier can be used anywhere in the class as required")
    print("It is not a rule to mention the private members first and then others") 
    print("It is just followed to write first for better readability.")
    print("thus,i will prefer you to go with option 3 i.e. 'Private specifier can be used anywhere in class'") 

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "3" or ans == "c":
        print("yes")

    elif ans == "50-50":
        print("opt1)                                                    opt2)Private specifier must be used before protected specifier")
        print("opt3)Private specifier can be used anywhere in class     opt4)")
        
        ans = input("now plz enter your ans")

        if ans == "3" or ans =="c":
            print("yes")
    
elif ans == "50-50":
    print("opt1)                                                        opt2)Private specifier must be used before protected specifier")
    print("opt3)Private specifier can be used anywhere in class         opt4)")
    
    ans = input("now plz enter your ans")

    if ans == "3" or ans =="c":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("The private specifier can be used anywhere in the class as required")
        print("It is not a rule to mention the private members first and then others") 
        print("It is just followed to write first for better readability.")
        print("thus,i will prefer you to go with option 3 i.e. 'Private specifier can be used anywhere in class'") 

        if ans == "3" or ans =="c":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '10 SAWAAL',poore'$3,20,000'ke liye, apke saamne yeh raha\n")
print("How many basic types of inheritance are provided as OOP feature?")
print("opt1)1                                        opt2)4")
print("opt3)2                                        opt4)3")

ans = input("enter yr ans: ").strip().lower()

if ans == "2" or ans == "b":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("There are basically 4 types of inheritance provided in OOP, namely")
    print("single level, multilevel, multiple and hierarchical inheritance")
    print("We can add one more type as Hybrid inheritance but that is actually")
    print("the combination any types of inheritance from the 4 basic ones")
    print("thus,i will prefer you to go with option 2 i.e. '4'") 



    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "2" or ans == "b":
        print("yes")

    elif ans == "50-50":
        print("opt1)          opt2)4")
        print("opt3)2         opt4)")
        
        ans = input("now plz enter your ans")

        if ans == "2" or ans =="b":
            print("yes")
    
elif ans == "50-50":
    print("opt1)         opt2)4")
    print("opt3)2         opt4)")
    
    ans = input("now plz enter your ans")

    if ans == "2" or ans =="b":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("There are basically 4 types of inheritance provided in OOP, namely")
        print("single level, multilevel, multiple and hierarchical inheritance")
        print("We can add one more type as Hybrid inheritance but that is actually")
        print("the combination any types of inheritance from the 4 basic ones")
        print("thus,i will prefer you to go with option 2 i.e. '4'") 


        if ans == "2" or ans =="b":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '11 SAWAAL',poore'$6,40,000'ke liye, apke saamne yeh raha\n")
print("Which programming language doesn’t support multiple inheritance?")
print("opt1)C++ and Java                              opt2)C and C++")
print("opt3)Java and SmallTalk                        opt4)Java")

ans = input("enter yr ans: ").strip().lower()

if ans == "4" or ans == "d":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("Java doesn’t support multiple inheritance")
    print("But that feature can be implemented by using the interfaces concept")
    print("Multiple inheritance is not supported because of diamond problem and similar issues")
    print("thus,i will prefer you to go with option 4 i.e. 'Java'")

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "4" or ans == "d":
        print("yes")

    elif ans == "50-50":
        print("opt1)         opt2)C and C++")
        print("opt3)         opt4)Java")
        
        ans = input("now plz enter your ans")

        if ans == "4" or ans =="d":
            print("yes")
    
elif ans == "50-50":
    print("opt1)         opt2)C and C++")
    print("opt3)         opt4)Java")
    
    ans = input("now plz enter your ans")

    if ans == "4" or ans =="d":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("Java doesn’t support multiple inheritance")
        print("But that feature can be implemented by using the interfaces concept")
        print("Multiple inheritance is not supported because of diamond problem and similar issues")
        print("thus,i will prefer you to go with option 4 i.e. 'Java'")

        if ans == "4" or ans =="d":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '12 SAWAAL',poore'$12,50,000'ke liye, apke saamne yeh raha\n")
print("Which type of inheritance leads to diamond problem?")
print("opt1)Multiple                                        opt2)Single level")
print("opt3)Multi-level                                     opt4)Hierarchical")

ans = input("enter yr ans: ").strip().lower()

if ans == "1" or ans == "a":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("When 2 or more classes inherit the same class using multiple inheritance")
    print("and then one more class inherits those two base classes")
    print("we get a diamond like structure. Here, ambiguity arises when same function gets derived into 2 base classes")
    print("and finally to 3rd level class because same name functions are being inherited")
    print("thus,i will prefer you to go with option 1 i.e. 'Multiple'")

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "1" or ans == "a":
        print("yes")

    elif ans == "50-50":
        print("opt1)Multiple         opt2)Single level")
        print("opt3)                 opt4)")
        
        ans = input("now plz enter your ans")

        if ans == "1" or ans =="a":
            print("yes")
    
elif ans == "50-50":
    print("opt1)Multiple             opt2)Single level")
    print("opt3)                     opt4)")
    
    ans = input("now plz enter your ans")

    if ans == "1" or ans =="a":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("When 2 or more classes inherit the same class using multiple inheritance")
        print("and then one more class inherits those two base classes")
        print("we get a diamond like structure. Here, ambiguity arises when same function gets derived into 2 base classes")
        print("and finally to 3rd level class because same name functions are being inherited")
        print("thus,i will prefer you to go with option 1 i.e. 'Multiple'")

        if ans == "1" or ans =="a":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '13 SAWAAL',poore'$25,00,000'ke liye, apke saamne yeh raha\n")
print("Which among the following is the language which supports classes but not polymorphism?")
print("opt1)SmallTalk                                opt2)Java")
print("opt3)C++                                      opt4)Ada")

ans = input("enter yr ans: ").strip().lower()

if ans == "4" or ans == "d":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("Ada is the language which supports the concept of classes but doesn’t support the polymorphism feature")
    print("It is an object-based programming language. Note that it’s not an OOP language")
    print("thus,i will prefer you to go with option 4 i.e. 'Ada'")

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "4" or ans == "d":
        print("yes")

    elif ans == "50-50":
        print("opt1)SmallTalk         opt2)")
        print("opt3)                  opt4)Java")
        
        ans = input("now plz enter your ans")

        if ans == "4" or ans =="d":
            print("yes")
    
elif ans == "50-50":
    print("opt1)SmallTalk         opt2)")
    print("opt3)                  opt4)Java")
    
    ans = input("now plz enter your ans")

    if ans == "4" or ans =="d":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("Ada is the language which supports the concept of classes but doesn’t support the polymorphism feature")
        print("It is an object-based programming language. Note that it’s not an OOP language")
        print("thus,i will prefer you to go with option 4 i.e. 'Ada'")


        if ans == "4" or ans =="d":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '14 SAWAAL',poore'$50,00,000'ke liye, apke saamne yeh raha\n")
print("If same message is passed to objects of several different classes and all of those can respond in a different way,what this feature called?")
print("opt1)Polymorphism                                        opt2)Inheritance")
print("opt3)Overloading                                          opt4)Overriding")

ans = input("enter yr ans: ").strip().lower()

if ans == "1" or ans == "a":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("The feature defined in question defines polymorphism features")
    print("Here the different objects are capable of responding to the same message in different ways, hence polymorphism.")
    print("thus,i will prefer you to go with option 1 i.e. 'Polymorphism'")
    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "1" or ans == "a":
        print("yes")

    elif ans == "50-50":
        print("opt1)Polymorphism        opt2)")
        print("opt3)                    opt4)Overriding")
        
        ans = input("now plz enter your ans")

        if ans == "1" or ans =="a":
            print("yes")
    
elif ans == "50-50":
    print("opt1)Polymorphism        opt2)")
    print("opt3)                    opt4)Overriding")
    
    ans = input("now plz enter your ans")

    if ans == "1" or ans =="a":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("The feature defined in question defines polymorphism features")
        print("Here the different objects are capable of responding to the same message in different ways, hence polymorphism.")
        print("thus,i will prefer you to go with option 1 i.e. 'Polymorphism'")

        if ans == "1" or ans =="a":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '15 SAWAAL',poore'$1,00,00,000'ke liye, apke saamne yeh raha\n")
print("Which among the following can’t be used for polymorphism?")
print("opt1)Member functions overloading             opt2)Static member functions")
print("opt3)Predefined operator overloading          opt4)Constructor overloading")

ans = input("enter yr ans: ").strip().lower()

if ans == "2" or ans == "b":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("Static member functions are not property of any object")
    print("Hence it can’t be considered for overloading/overriding")
    print("For polymorphism, function must be property of object, not only of class.")
    print("thus,i will prefer you to go with option 2 i.e. 'Polymorphism'")

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "2" or ans == "b":
        print("yes")

    elif ans == "50-50":
        print("opt1)         opt2)Static member functions")
        print("opt3)         opt4)Constructor overloading")
        
        ans = input("now plz enter your ans")

        if ans == "2" or ans =="b":
            print("yes")
    
elif ans == "50-50":
    print("opt1)         opt2)Static member functions")
    print("opt3)         opt4)Constructor overloading")
    
    ans = input("now plz enter your ans")

    if ans == "2" or ans =="b":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("Static member functions are not property of any object")
        print("Hence it can’t be considered for overloading/overriding")
        print("For polymorphism, function must be property of object, not only of class.")
        print("thus,i will prefer you to go with option 2 i.e. 'Polymorphism'")

        if ans == "2" or ans =="b":
            print("yes")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '16 SAWAAL',poore'$5,00,00,000'ke liye, apke saamne yeh raha\n")
print("Which problem may arise if we use abstract class functions for polymorphism?")
print("opt1)All classes are converted as abstract class      opt2)Derived class must be of abstract type")
print("opt3)Derived classes can’t redefine the function      opt4)All the derived classes must implement the undefined functions")

ans = input("enter yr ans: ").strip().lower()

if ans == "4" or ans == "d":
    print("yes")
    
elif ans == "EXPERT ADVICE":
    print("The undefined functions must be defined is a problem")
    print("because one may need to implement few undefined functions from abstract class")
    print("but he will have to define each of the functions declared in abstract class")
    print("Being useless task, it is a problem sometimes.")

    ans = input("now plz enter your ans").strip().lower()
    
    if ans == "4" or ans == "d":
        print("yes")

    elif ans == "50-50":
        print("opt1)All classes are converted as abstract class         opt2)")
        print("opt3)                                                    opt4)All the derived classes must implement the undefined functions")
        
        ans = input("now plz enter your ans")

        if ans == "4" or ans =="d":
            print("yes")
    
elif ans == "50-50":
    print("opt1)All classes are converted as abstract class         opt2)")
    print("opt3)                                                    opt4)All the derived classes must implement the undefined functions")

    
    ans = input("now plz enter your ans")

    if ans == "4" or ans =="d":
        print("yes")

    elif ans == "EXPERT ADVICE":
        print("The undefined functions must be defined is a problem")
        print("because one may need to implement few undefined functions from abstract class")
        print("but he will have to define each of the functions declared in abstract class")
        print("Being useless task, it is a problem sometimes.")


        if ans == "4" or ans =="d":
            print("yes")
else:
    print("no")
exit()

