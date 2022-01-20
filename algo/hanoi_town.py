# import fire

def hanoi_tw(ndisk, from_peg, to_peg):
    if ndisk == 1:
        print("Move disk from peg {0} to peg {1}".format(from_peg, to_peg))
        return
    unset_peg = 6 - from_peg - to_peg
    hanoi_tw(ndisk - 1,  from_peg, unset_peg)
    print("Move disk from peg {0} to peg {1}".format(from_peg, to_peg))
    hanoi_tw(ndisk - 1,  unset_peg, to_peg)
    return

args = []
args.append(int(input("Enter Disk Number:")))
args.append(int(input("Enter From Peg Number:")))
args.append(int(input("Enter To Peg Number:")))

hanoi_tw(*args)

# def hello(n):
#     print("help {0}".format(n))

# if __name__ == '__main__':
#     fire.Fire(hello)
