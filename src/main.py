from raspgierry_pi import RaspgierryPi

def main(argv=[]):
    game = RaspgierryPi()
    game.run()  
       
if __name__ == "__main__":
    from sys import argv
    main(argv)
