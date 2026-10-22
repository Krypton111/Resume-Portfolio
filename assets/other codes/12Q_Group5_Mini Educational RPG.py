import random

while True:

      print("\n\nWelcome to the world of QuestMasters!")
      print("An educational RPG game to enhance your learning!\n")
      ask = input("Would you like to start the game (yes/no): ")
      menu_page = ("Start Game", "Extras", "Exit")

      if ask.lower() == "yes" or ask.lower() == "y":
          print(menu_page)
          menu = input("Enter 'Start Game' to begin, 'Extras' for more options, or 'Exit' to quit: ")

          if menu.lower() == "start game":
              name = input("Hello dear player, what is your name?: ") 
              country = input("What nation/country are you from?: ")
              print("Welcome aboard, " + name + "!")
              print("Mr. Kevin: I am Mr. Kevin and I will be your flight attendant for today.")
              print("---------------")
              print("BOARDING PASS")
              print("~~ ✈️ ", "KerwinBlaise Airlines ✈️ ~~")
              print("🎫 ", "Passenger Name: " + name)
              print("🎫 ", "from " + country)
              print("🎫 ", "to [0f$3k2;d]")
              print("🎫 ", "Seat Number: 54E ", "Gate: A20")
              print("---------------")
              print("It seems like you will be flying to [REDACTED] today, " + name + ".")
              input("Type any key to continue: ")

              print("---------------")
              print("Mr. Kevin: Passenger " + name + "," , "I hope you will enjoy this adventure :).")
              print("---------------")
              input("Type any key to continue: ")

              print("---------------")
              print(" O Ol ;O: :O;  ;_:PD-;_:_POkL:Jo LolP:;O_")
              print("4;plfeosfdlp awfsf ")
              print("---------------")
              input("Type any key to continue: ")

              print("---------------")
              print("Mr. Kevin: Oh no, what's happening?!")
              print("Mr. Kevin: I have a feeling that something is wrong with the plane, but I don't know what it is!!!")
              print("---------------")
              input("Type any key to continue: ")

              print("---------------")
              print("🧛🧛‍♂️👄🧛‍♂️🧛🧛👄🧛‍♂️")
              print("👄🧛‍♂️🧛🧛👄🧛‍♂️")
              print("🧛‍♂️🧛👄🧛‍🧛")
              print("---------------")
              input("Type any key to continue: ")

              print("---------------")
              print("Oh no! It seems like the plane has been infested with vampires.")
              print("It is now your duty, " + name + " to save the people inside this trip")
              print("by defeating the vampires through answering general knowledge questions!")
              print("---------------")
              input("Type any key to continue: ")

              print("---------------")
              print("You will go through different levels of this game, with each question getting difficult as the level goes by.")
              print("You will just type the correct LETTER of the answer you think is correct.")
              print("Best of luck, and I hope you will arrive safely on your destination to [REDACTED].")
              print("---------------")

          elif menu.lower() == "extras":
              print("---------------")
              print("ABOUT THE TEAM")
              print("We are the Team High5")
              print("because we are Group 5.")
              print("This team consists of: ")
              team = ["Kerwin Concepcion",
                      "Johann Manzano",
                      "Mark Macascas",
                      "Riam Santiago",
                      "Irene Nuñez",
                      "Jamaya Cordova"
                     ]
              for member in team:
                  print(member)
              print("We hope that you will enjoy this game.")
              print("---------------")
              input("Type any key to return to the main menu: ")
              continue

          elif menu.lower() == "exit":
              print("Thank you for playing!")
              break

          else:
              print("Invalid input. Please only type yes or no.")
              continue

      elif ask.lower() == "no" or ask.lower() == "n":
          print("Okay, thank you for your time")
          break

      else:
          print("Invalid input. Please only type yes or no.")
          continue

      def trivia_question(level):
        # Define questions and answers based on difficulty level
        if level == 1:
          questions = [
          "Who discovered the theory of relativity?",
          "Which current capital in the world has the most population?",
          "What is the value of π? (first three digits)"
          ]
          answers = ["a", "b", "c"]
          choices = ["(a) Albert Einstein", "(b) China", "(c) 3.14"]
        elif level == 2:
          questions = [
          "What is the capital of Australia?",
          "Who painted the Mona Lisa?",
          "What is the powerhouse of the cell?"
          ]
          answers = ["a", "b", "c"]
          choices = ["(a) Canberra", "(b) Leonardo da Vinci", "(c) Mitochondria"]
        elif level == 3:
          questions = [
          "Who is the author of 'To Kill a Mockingbird'?",
          "What is the largest organ in the human body?",
          "What is the chemical symbol for water?"
          ]
          answers = ["a", "b", "c"]
          choices = ["(a) Harper Lee", "(b) Skin", "(c) H2O"]
        elif level == 4:
          questions = [
          "Who is the current president of the United States?",
          "What is the largest planet in the solar system?",
          "Who wrote 'The Odyssey'?"
          ]
          answers = ["a", "b", "c"]
          choices = ["(a) Joe Biden", "(b) Jupiter", "(c) Homer"]
        elif level == 5:
          questions = [
          "Who is the inventor of the telephone?",
          "What is the chemical element with atomic number 1?",
          "What is the square root of 81?"
          ]
          answers = ["a", "b", "c"]
          choices = ["(a) Alexander Graham Bell", "(b) Hydrogen", "(c) 9"]
        elif level not in range (1,49):
          questions = ["W̸h̶a̵t̴ ̴is̸ ̷t̸h̸e̶ ̵m̷ea̴n̸in̷g̷ ̶o̷f̷ ̸y̸o̶u̴r̷ ̸e̶x̷is̸te̶n̷c̴e̸? ?"]
          answers = ["m̵͓̼̱͛e̸͈̓a̴̳̱̋̈́n̸̬͂̍̃ȉ̶̬̝̈́n̷̤̳̪̊͝g̶̨͕͉͆̄͗l̴̪͗ë̵͙́̋s̷̞̗̈́͜͝͠s̴̼̫̖̃̅͑m̸̡̰͊̆͐e̵̙͌a̸̛̦̼̞̎n̸̯͕̟̊i̶͇̹͚͝n̴̨̓g̷̦̖͗̀l̴͔̗̾ę̷͆̈̿s̵͓̿ś̴̹m̵̘̌ḙ̷̛͂a̸̡̎͜n̷͉͖͆̑͜i̴͚̳̾͂͝ñ̷̞̗ḡ̸̬͎ͅl̷̤̲̽̊͒é̴̩̈́s̷̻͝ś̶̙͙̦̄͋m̶̻̔e̴̡͖͐͝ȃ̷̛̩͘n̶̛̺͔͉̓́i̶̢̥͌͌͌n̷̛̖̞g̸͔̍́l̶̔̔͗͜e̵̪͔̒ṣ̶͝s̷̲͙̺͛"]
          choices = ("l̷͍͇̟̟͚̻͈͋̇̓͂̕i̶̼͎͕͊f̷̡̮̬̗͂̇̍̎̄̕͝ę̵̖͔̺͂̑l̸̡͔̙̹̲͊͂̊ͅi̶̭̒̊̇̓͗̍̍͜f̸͚͕͉̃͛̉̀̚ē̸̤̱̯̐̿͒l̶̼̦͔͎̅̈́̚ḯ̴͚͓̜̭̥̥͜f̶̳̂̃̍e̵̖̍̏̈́̚l̴̝̯̄̇̍̚i̵͕̼͙̜̍f̸̛̰̹̬̅͒͒́̊͜ẻ̴̢̧͚̠̹̻̌ͅl̴̜̘̊̈́̿̿̂̚i̷̧̘̦̺̹̻̩̇f̴͓̀̂̓̽ẹ̷͆̀͛l̷̰͈͓̪͖̏̋̅̈͊̇̔ï̷̬͖͛̂̂͘f̶̡̛͖̜͎̮͔̻̿͐̎̽͂̌ȩ̸͙̭̟̔̈͒͠l̷͖̈́̂i̴͕͎̞̥̠̼̽́f̴̹͉̣̣̩̐ĕ̴̡̟͕͒m̵̟̟̥̼̈́̔́̃̇̕͘ͅe̷̠̋̀̂̕a̷͎̟͍͉̔͌̾̆̃̂̉ͅn̸̨͙̣͍͈͉̰͊͂͑̓͘ĭ̶̦̼̥͒͂̍͠͝n̷͍̐̌̐̎ğ̷̺̲̄l̴͓̓̓ȇ̶̛̞̯̞͙̖͍̑̈́̊̾̚s̵̩̥̟̜̋̀͑̚͝͝ş̶̢͓̪̐m̴̞̹̩̤̼̍̽̉͠e̵͔̤͋̿̑̓́a̶̡̺͓͋̀̏̇n̷͕͚̗͙͚͙͂̅̈́̾̈́ḯ̷̯̥̈̽̓̌͊̕ǹ̴̜̝̼̭̤̱g̴̙͔͆̓͗̑͑̾͝ͅͅl̴̜̆́̚͝ḛ̴͕̞̇̄̿̑͑ṩ̸͕̓̅s̴͚͓̋̈͘͘ṁ̵̝͉͂́̑̍̄e̸͔͈̼͍̬̜̲̒̀́̆͛͝a̶̛͈͙ņ̷̧̠͎̞͚̰͒i̴̤̳͕̠̼͖͘͘͠ń̵̝͇̯̜͚̠̼̑̏̐̕͠g̶̯̉͋̋͒̇͑l̷̡͓̠̻̼͌̒́̂̇̕͝e̵̮̹̲̞͊͑͜s̷̢͇̘̳͇̓̿̆s̴͇͔̱̦̮͈̾̆̎l̷͓͍̩̞̟̾́ì̶̧̛̠̪̫͔͓̦̂̀̓f̵̗̱̬̪̓́̂̂̎̌ȩ̷̨̗̬͎͚͈̿l̵͓͇͙͉̖̟͑i̴̤̥͖̩͆͒̅͠f̴̜̀̈ė̸̻̘̻̎͑̄͛̈͠ͅl̶͙̂͛͒̆͘͠i̶̯̦͓̼͌̈́̑̓ͅf̸͙̭̮̒̾̊́͜e̴͈̦̓̍̂̂͗̇̚l̸̛͖͔̋̓̿͘ͅï̴̝͖̬̺͕̖̺̅̆̀̎ḟ̸̯̠̭̭̤̯͕͋͂e̵̫̟̩͍̮͒͊͋͊̈́͝͝l̴̛̼̓͛͛̓́î̶̱͆̀̀̔f̶̬̭̩̪̩̞̝͂̾ẽ̵̡̱̯͚̤̻̘̏͑̍̚l̷̹̩̮̦̩̫͛͗̐͋̈́i̵̞̍̀̄͌̈́̆f̸̨̝͖̻̼͚͖͆̽̒̌ę̶͌̀͝l̴͕̼̀̃̆͘͜i̴͚͇̭͙͋̌̋͠f̸̥̆̆̕ę̶̭̖͓͓͕̀̿͌ͅ")
        else:
          questions = [
        "Who discovered the theory of relativity?",
        "Which current capital in the world has the most population?",
        "What is the value of π? (first three digits)",
        "What is the capital of Australia?",
        "Who painted the Mona Lisa?",
        "What is the powerhouse of the cell?",
        "Who is the author of 'To Kill a Mockingbird'?",
        "What is the largest organ in the human body?",
        "What is the chemical symbol for water?",
        "Who is the current president of the United States?",
        "What is the largest planet in the solar system?",
        "Who wrote 'The Odyssey'?",
        "Who is the inventor of the telephone?",
        "What is the chemical element with atomic number 1?",
        "What is the square root of 81?",
        "Who is the current prime minister of Canada?",
        "What is the smallest planet in the solar system?",
        "What is the speed of light in a vacuum?",
        ]
          answers = ["Albert Einstein", "China", "3.14", "Canberra", "Leonardo da Vinci", "Mitochondria", "Harper Lee", "Skin", "H2O", "Joe Biden", "Jupiter", "Homer", "Alexander Graham Bell", "Hydrogen", "9", "Justin Trudeau", "Mercury", "299,792,458 m/s"]
          choices = ("guess the right answer >:)")

        while True:
          #chooses a question at random (goes hand in hand with import random)
          idx = random.randint(0, len(questions) - 1)
          question = questions[idx]
          correct_answer = answers[idx]

          #asks the random question
          print("    QUESTION:", question)
          print("")
          print("    CHOICES:", choices)
          print("")
          user_answer = input("    YOUR ANSWER: ").lower()
          print("")

          #sys check of answer is correct
          if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            return True
          elif user_answer.lower() in answers:
            print("Incorrect!")
            return False
          else:
            print("Invalid input. Please try again.")
            return False

      def main():

        experience = 0
        level = 1
        points = 0

        while True:
          print("\nSTATS:")
          print("Level:", level)
          print("Experience:", experience)
          print("Points:", points)
          print("")

          #level up system (like rebirth)
          if trivia_question(level):
            experience += 10
            points += 1
          if experience >= 50:
            level += 1
            experience = 0
            print("Congratulations! You've leveled up to level", level)
            input("Press Enter to continue...")
          if level == 6:
            print("Achievement Unlocked: QuestMaster")
            input("Press Enter to continue...")
          if level == 10:
            print("Achievement Unlocked: Real Quest Master!")
          if level == 15:
            print("Achievement Unlocked: Unending Glory!")
          if level == 20:
            print("Achievement Unlocked: You should probably stop playing now...")
          if level == 25:
            print("Achievement Unlocked: why? No, just no...")
          if level == 30:
            print("Achievement Unlocked: get a life.")
          if level == 35:
            print("Achievement Unlocked: I'm done giving you achievements. bye.")
          if level >= 50:
            print("\n Achievement Unlocked: ??? y̷o̷u̶ ̸a̶r̷e̵ ̸n̴o̴t̸ ̸s̵u̸p̴p̸o̶s̵e̶d̷ ̴t̶o̶ ̵b̵e̴ ̶h̵e̸r̸e̵ ʕ̡̢̡ʘ̅͟͜͡ʘ̲̅ʔ̢̡̢ ლↂ‿‿ↂლ ᕦ⊙෴⊙ᕤ (╬ಠิ益ಠิ) (༎ຶꈊ༎ຶ╬)（థ ՞ਊ ՞）థ ༽つ۞﹏۞༼つ༽つ(ง ͠° ͟ل͜ ͡°)ง (ง \n")

          # Saves the player's points, level, experience, and previous answer in a text file
          file = open("player_data.txt", "w")
          file.write("Points: {}\nLevel: {}\nExperience: {}\n".format(points, level, experience))
          file.close()

          # Does the player still want to continue
          while True:
              try:
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again == 'n' or play_again == 'no':
                  print("Thanks for playing!")
                  return
                elif play_again == 'y' or play_again == 'yes':
                  break
                else:
                  raise ValueError("Invalid input. Please enter 'y' or 'n'.")
              except ValueError as e:
                print("Error:", e)

        # to tie up the whole code
      if __name__ == "__main__":
        main()

