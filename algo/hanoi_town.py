
def honoi_tw(ndisk, from_peg, to_peg):
    if ndisk == 1:
        print("Move disk from peg {0} to peg {1}".format(from_peg, to_peg))
        return
    unset_peg = 6 - from_peg - to_peg
    honoi_tw(ndisk - 1,  from_peg, unset_peg)
    print("Move disk from peg {0} to peg {1}".format(from_peg, to_peg))
    honoi_tw(ndisk - 1,  unset_peg, to_peg)
    return

honoi_tw(3, 1, 3)


