import random


class RandomGenerator:
    def random_seedless(a, b):
        c = random.randrange(a, b)
        return c

    def random_seed(a, b, seed):
        random.seed(seed)
        c = random.randrange(a, b)
        return c

    def random_list(a, b, n):
        rlist = []
        for i in range(0, n):
            x = random.randrange(a, b)
            rlist.append(x)
        return rlist

    def random_list_seed(a, b, n, seed):
        rlist = []
        c = random.seed(seed)
        for i in range(0, n):
            x = random.randrange(a, b)
            rlist.append(x)
        return rlist

    def random_item(rlist):
        return random.choice(rlist)

    def random_item_seed(rlist, seed):
        random.seed(seed)
        return random.choice(rlist)

    def random_select(r, a):
        return random.sample(r, a)

    def random_select_seed(r, a, seed):
        random.seed(seed)
        return random.sample(r, a)