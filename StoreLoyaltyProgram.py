"""
Store Loyalty Program.
Credits to Brendan Scott Feb 2015, as this
program is partly derived from his address
book.
"""

## Imports
import time
from os import system as command101
command101("clear")
## Error Classes


class TransactionError(Exception):
    pass


class CannotPay(TransactionError):
    pass


class PickleError(Exception):
    pass


## Variables

id_s = {}

## Functions


def clear():
    command101("clear")


def check_good(filename, written, p):
    with open(filename, "r") as read:
        if p.load(read) != written:
            return False
        return True


def super_dump(filename, to_write):
    import pickle as p
    try:
        with open(filename, "w") as write:
            p.dump(write, to_write)
    except:
        with open(filename, "w") as write:
            write.write(str(p.dumps(to_write))[2:-1])
    if not check_good(filename, to_write, p):
        raise PickleError


def super_load(filename):
    import pickle as p
    try:
        with open(filename, "r") as read:
            return p.load(read)
    except:
        with open(filename, "r") as read:
            return p.loads(read.read())

def use(text):
    return input(text)

def trans(customer_id, amount_to_add_to_balance):
    atatb = amount_to_add_to_balance  ## Amount To Add To Balance (ATATB)
    try:
        return [True, id_s[customer_id].make_transaction(atatb)]
    except:
        return [False, None]

## Security
x="""class String(object):
    def __init__(self, string):
        self.my_list=list(string)
    def get(self):
        return ''.join(self.my_list)
def secure_use(text):
    return String(use(text))
the_password=secure_use("PASSWORD: ")
print(the_password.get())
if the_password != String(str(hash("password"))):
    print("Locked out!")
    print(p.dumps(use("PASSWORD: ")))
    from sys import exit;exit(1)"""
del x

## Get The Date

if __name__ == "__main__":
    print("Welcome to the Store VIP Interface")
    year = use("Year (0 to 9999): ")
    clear()
    print("Welcome to the Store VIP Interface")
    month = use("Month (1 to 12): ")
    clear()
    print("Welcome to the Store VIP Interface")
    day = use("Day (1 to 31): ")
    clear()
    year = year.zfill(4)
    month = month.zfill(2)
    day = day.zfill(2)
    date = "/".join([day, month, year])

## Misc. Classes


class Person(object):
    """class Person(self, first_name, last_name[, credit_card=False, uses_cash=True, default='cash'])
  Creates a Person() class
  'default' variable may be 'card' or 'cash'"""

    def end(self):
        id_s[self.person_id] = self

    def __init__(self,
                 first_name,
                 last_name,
                 credit_card=False,
                 uses_cash=True,
                 default="cash"):
        self.person_id = id(self)
        self.first = first_name
        self.last = last_name
        self.name = first_name + " " + last_name
        self.uses_cash = uses_cash
        self.default = default
        self.mytype = "adult"
        if credit_card == False:
            self.mytype = "child"
        ## ' credit_card ' is the same as ' self.mytype=='adult' '
        if self.mytype == "adult" or uses_cash:
            self.transactions = []
        self.end()

    def make_transaction(self, amount):
        if not self.mytype == "adult" or self.uses_cash:
            raise CannotPay
        if self.mytype == "child":
            how_to_pay = "cash"
        else:
            if self.uses_cash:
                how_to_pay = self.default

        x = repr(self.__class__)[17:-2].lower()
        my_transaction = Transaction(amount, date, self.person_id, how_to_pay,
                                     x)
        self.transactions.append(my_transaction)
        self.end()
        return my_transaction

    def get_balance(self):
        bsf = 0  # Balance So Far (BSF)
        for i in self.transactions:
            i = i.aatb
            bsf += i
        return bsf

    def __repr__(self):
        return 'Person(first_name=%r,' % self.first + ' last_name=%r' % self.last + ', credit_card=%s,' % (
            [self.mytype == 'adult'][0].__repr__(), ) + ' uses_cash=%s,' % (
                self.uses_cash.__repr__(), ) + ' default=%r, ' % (self.default) + 'balance=%i'%self.get_balance()


class PersonBook(object):
    def __init__(self):
        self.organised_people = {"Person": [], "Business": [], "Family": []}
        self.people = []

    def add_people(self, people):
        for person in people:
            self.people.append(person)
            x = repr(person.__class__)[17:-2]
            y = self.organised_people[x][:]
            y.append(person)
            self.organised_people[x] = y

    def __getitem__(self, item):
        return self.people.__getitem__(item)


class TransactionBook(object):
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


class Business(Person):
    def __init__(self, credit_card):
        self.person_id = id(self)


class Family(Person):
    def __init__(self, people):
        self.person_id = id(self)


class Transaction(object):
    def __init__(self, amount_added_to_balance, date, customer_id, pay_method,
                 my_type):
        self.aatb = amount_added_to_balance
        self.date = date
        self.customer = id_s[customer_id]
        self.customer_type = my_type
        self.pay_method = pay_method


class Controller(object):
    def add_person(self):
        ## Credit Card y/N
        ## Uses Cash Y/n
        ## Default ("card" or "CASH")
        quit = "q!"
        x = "Type '%s' at any time when asked for inputto quit." % quit
        print(x)
        t = "Type the new person's %s. >>> "
        first_name = use(t % "first name")
        if first_name == quit:
            print("Not Adding")
            return ""
        clear()
        print(x)
        last_name = use(t % "last name")
        if last_name == quit:
            print("Not Adding")
            return ""
        clear()
        print(x)
        credit_card = use(
            "Does the new person have a credit card? (y/N) ").lower()
        if credit_card == quit:
            print("Not Adding")
            return ""
        elif credit_card in ["y", "yes", "yeah"]:
            credit_card = True
        else:
            credit_card = False
        clear()
        print(x)
        uses_cash = use("Does the new person use cash? (Y/n) ").lower()
        if uses_cash == quit:
            print("Not Adding")
            return ""
        elif uses_cash in ["n", "no", "nah"]:
            uses_cash = False
        else:
            uses_cash = True
        clear()
        print(x)
        default = use("Default pay option? (card/CASH) ").lower()
        if default == quit:
            print("Not Adding")
            return ""
        elif default != "card":
            default = "cash"
        my_person = Person(first_name, last_name, credit_card, uses_cash,
                           default)
        self.person_book.add_people([my_person])

    def make_transaction(self):
        trans_run = True
        print("To make a transaction, type 'make'. ")
        print("To see a Customer ID->Customer mapping, type 'mapping'. ")
        print("To see these instructions again, type 'instruct'. ")
        print("Anything else will be regarded as quitting. ")
        while trans_run:
            your_input = use("Store VIP Interface\n" +
                             ["-" * 30][0] + "\nconsole> ")
            if your_input == "mapping":
                for i in id_s: print("ID " + str(i) + ": " + id_s[i].__repr__())
                time.sleep(10)
            elif your_input == 'instruct':
                print("To make a transaction, type 'make'. ")
                print(
                    "To see a Customer ID->Customer mapping, type 'mapping'. ")
                print("To see these instructions again, type 'instruct'. ")
                print("Anything else will be regarded as quitting. ")
            elif your_input == "make":
                id_control = int(use("Customer ID: "))
                if id_control not in id_s.keys():
                    print("Error! ID doesn't exist.")
                    self.make_transaction()
                    return None
                else:
                    amount_control = int(
                        use("Amount to add (for paying put negative): "))
                    trans(id_control, amount_control)
            else:
                trans_run = False
            if trans_run and your_input != "instruct":
                clear()

    def error(self, your_input, err_msg):
        print("Cannot recogonise command (%s)" % your_input)
        print("Error:\n%s" % err_msg)

    def confirm_quit(self):
        if use("Are you sure you want to quit? (y/N)").lower() in [
                "y", "yes", "absolutely", "definitely", "100%", "yeah", "100"
        ]:
            return True
        return False

    def run_interface(self):
        instructions = """Type 'add' to add a person.
Type 'pay' to make a transaction.
Type 'quit' to quit."""
        running = True
        things = {
            "add": self.add_person,
            "pay": self.make_transaction
        }
        while running:
            clear()
            print(instructions)
            my_input = use(">>> ")
            clear()
            if my_input == 'quit':
                running = False if self.confirm_quit() else True
            else:
                try:
                    things[my_input]()
                except BaseException as msg:
                    self.error(my_input, msg)
        for spam in range(10):
            for eggs in range(4):
                clear()
                print("Saving people" + ["." * [eggs - 1][0]][0])
                time.sleep(1)
                if spam == 9 and eggs == 3:
                    super_dump("person.txt", self.person_book)
        for spam in range(10):
            for eggs in range(4):
                clear()
                print("Saving transactions" + ["." * [eggs - 1][0]][0])
                time.sleep(1)
                if spam == 9 and eggs == 3:
                    super_dump("transaction.txt", self.transactions)

    def __init__(self):
        ## PersonBook
        try:
            self.person_book = super_load("person.txt")
        except:
            self.person_book = PersonBook()
        ## Transaction_book
        try:
            self.transactions = super_load("transaction.txt")
        except:
            self.transactions = TransactionBook()
        self.run_interface()


## Main Section
if __name__ == "__main__":
    controller = Controller()
