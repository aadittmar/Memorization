import os
import sys

def add_verses_to_dict():
    # Put dictionaries of all chapter's verses into main chapters dictionary
    romans_chapters_dict[1] = romans_1_dict
    romans_chapters_dict[2] = romans_2_dict
    romans_chapters_dict[3] = romans_3_dict
    romans_chapters_dict[4] = romans_4_dict
    romans_chapters_dict[5] = romans_5_dict
    romans_chapters_dict[6] = romans_6_dict
    romans_chapters_dict[7] = romans_7_dict


    # Set up Romans 1 Dictionary for all verses
    romans_1_dict[ 1 ] = "Paul, a servant of Christ Jesus, called to be an apostle and set apart for the gospel of God—"
    romans_1_dict[ 2 ] = "the gospel he promised beforehand through his prophets in the Holy Scriptures"
    romans_1_dict[ 3 ] = "regarding his Son, who as to his earthly life[a] was a descendant of David, "
    romans_1_dict[ 4 ] = "and who through the Spirit of holiness was appointed the Son of God in power[b] by his resurrection from the dead: Jesus Christ our Lord."
    romans_1_dict[ 5 ] = "Through him we received grace and apostleship to call all the Gentiles to the obedience that comes from[c] faith for his name’s sake."
    romans_1_dict[ 6 ] = "And you also are among those Gentiles who are called to belong to Jesus Christ."
    romans_1_dict[ 7 ] = "To all in Rome who are loved by God and called to be his holy people: Grace and peace to you from God our Father and from the Lord Jesus Christ."
    romans_1_dict[ 8 ] = "First, I thank my God through Jesus Christ for all of you, because your faith is being reported all over the world."
    romans_1_dict[ 9 ] = "God, whom I serve in my spirit in preaching the gospel of his Son, is my witness how constantly I remember you"
    romans_1_dict[ 10 ] = "in my prayers at all times; and I pray that now at last by God’s will the way may be opened for me to come to you."

    return

def option_menu():
    print("\nOptions:")
    print("   [1]: Memorize Individual Verses")
    print("   [2]: Entire Quiz\n")
    option = int(input("Choose an option (1 or 2):"))

    if option == 1:
        select_verse()

def select_verse():
    chapter        = 0
    verse          = 0
    selected_verse = ""

    try:
        chapter_verse = input("\nWhat chapter and verse are you trying to memorize (1:1, menu)? ")

        if "menu" in chapter_verse:
            option_menu()
        else:
            chapter = int(chapter_verse.split(":")[0])
            verse   = int(chapter_verse.split(":")[1])

    except:
        chapter_verse = 0
        chapter       = 0
        verse         = 0

    # check to see if chapter exists in romans_chapters_dict
    if chapter in romans_chapters_dict.keys():

        # check to see if verse exists in specific chapter dictionary
        if verse in romans_chapters_dict[chapter].keys():
            selected_verse = romans_chapters_dict[chapter][verse]
        else:
            print("\nThat is not a valid verse, please try again.\n")
            selected_verse = "unknown"
            select_verse()

    check_answer(selected_verse)

    return

def select_entire_chapter():
    # TODO: Make this!
    pass

def check_answer(selected_verse):

    # count how many times the user gets the verse right. After (10) times the program goes back to the menu.
    count = 0
    user_answer = input("\nPrint verse: ")

    while user_answer == selected_verse:
        count += 1

        if count >= 10:
            print("\nCongrats, you got it ", count, " times in a row!")
            option_menu()

        else:

            # Try to clear the screen. Only works on windows terminal right now.

            try:
                clear
            except:
                print("Clearing the screen did not work.")
            

            if count < 2:
                print("\nCorrect [", count, "] time")
            else:
                print("\nCorrect [", count, "] times")

            # ask the user to enter the verse again if they got it right the previous time.
            user_answer = input("\nPrint again: ")

    print("\nIncorrect. Correct answer is: ", selected_verse, "\n")
    select_verse()

    return

### START OF PROGRAM ###

# setup 'clear' command. Only works on Windows right now.
print("\nThis is a memorization tool for the NIV [2001] translation of the Bible.")

# Get the system type
system_type = str(sys.platform)

if system_type == "darwin":
    system_type = "OSX"
if system_type == "win32":
    system_type = "Windows"

# Setup the clear screen variable. Only works on Windows right now.
if system_type == "OSX":
    clear = lambda: os.system('clear')
elif system_type == "Windows":
    clear = lambda: os.system('cls')

# Create dictionaries for holding all verses
romans_chapters_dict= {}
romans_1_dict       = {}
romans_2_dict       = {}
romans_3_dict       = {}
romans_4_dict       = {}
romans_5_dict       = {}
romans_6_dict       = {}
romans_7_dict       = {}
add_verses_to_dict()

# go to the menu to select different options
option_menu()
