def main(argv=[]):
    game = RaspgierryPi()
    game.run()
       
if __name__ == "__main__":
    from sys import argv
    from sys import path
    from os.path import dirname as dir
    path.insert(0, dir(path[0]))
    from raspgierry_pi import RaspgierryPi
    main(argv)
