# coding:latin1

"""Log in module for application which need password and accounts
##    Name :  Tk_Log in Box
##    Version :  1.0
##    Autor :  Awounang Nekdem Franck
"""


class popup:
    """Class of popup messages"""

    def __init__(self, master=None, title="Error", message="Bad User name or Password\nplease try again!", delai=1250,
                 typ="error"):
        from tkinter import Label, Tk, PanedWindow
        from winsound import MessageBeep as snd
        lst = dict((("error", 10), ("info", 60), ("warning", 23), ("message", 75)))
        if master == None:
            master = Tk()
            master.title(title)
        frm = PanedWindow(master)
        frm.pack()
        lbl = Label(frm, text=message, width=24)
        lbl.pack()
        lbl.focus()
        if master.title() == title:
            lbl.after(delai, master.destroy)
        else:
            frm.after(delai, frm.destroy)
        try:
            snd(lst[typ])
        except:
            print("the arg '", typ, "' must be 'error','info','warning',or 'message'")
        frm.mainloop()


class login:
    """ classe de base de login-box utile pour une entrée de nouvel utilisateur

options standards:
-title:le titre de la boite de dialogue(texte)
-mask:le caractère qui sera présenté pour cacher les lettre du mot de passe

methodes /fonctions:
-show: affiche la boite de login et retourne les infos entrées par l'utilisateur
"""

    def __init__(self, title="Log in Box", mask="&"):
        """Constructor of login Box\nargs:title,selected"""
        from tkinter import Tk, Frame, Label, Entry, Button, BooleanVar, Checkbutton
        self.__Entry__ = Entry
        self.__usr__, self.__pwrd__ = None, None
        self.__mask__ = mask
        self.__root__ = Tk()
        self.__frm__ = Frame(self.__root__)
        self.__frm__.pack(side="top")
        self.__frm2__ = Frame(self.__root__)
        self.__frm2__.pack()
        self.__root__.title(title)
        self.__root__.resizable(False, False)
        self.__lbl_usr__ = Label(self.__frm__, text="User name : ", bd=4, relief="groove", width=13)
        self.__lbl_usr__.grid(row=1, column=1)
        self.__lbl_pwrd__ = Label(self.__frm__, text="Password : ", bd=4, relief="groove", width=13)
        self.__lbl_pwrd__.grid(row=2, column=1)
        self.__lbl_pwrd2__ = Label(self.__frm2__, text="Password again: ", bd=4, relief="groove", width=13)
        self.__lbl_pwrd2__.grid(row=1, column=1)
        self.__txt_usr__ = Entry(self.__frm__, width=15)
        self.__txt_usr__.grid(row=1, column=2)
        self.__txt_pwrd__ = Entry(self.__frm__, width=15, show=self.__mask__)
        self.__txt_pwrd__.grid(row=2, column=2)
        self.__txt_pwrd2__ = Entry(self.__frm2__, width=15, show=self.__mask__)
        self.__txt_pwrd2__.grid(row=1, column=2)
        self.__frm___ok_cancel = Frame(self.__root__, width=76)
        self.__frm___ok_cancel.pack(side="bottom")
        self.__btn_ok__ = Button(self.__frm___ok_cancel, text="Ok", width=6, command=self.__func_ok__)
        self.__btn_ok__.pack(side="left", padx=5)
        self.__var_check__ = BooleanVar(self.__root__, True)
        self.__check__ = Checkbutton(self.__frm___ok_cancel, text="Hide code",
                                     variable=self.__var_check__, command=self.__Check__)
        self.__check__.pack(side="left", padx=2)
        self.__btn_cancel__ = Button(self.__frm___ok_cancel, text="Cancel", width=6, command=self.__cancel__)
        self.__btn_cancel__.pack(side="right", padx=5)
        self.__root__.bind("<Escape>", self.__cancel__)
        self.__txt_usr__.bind("<Return>", self.__func_ok__)
        self.__txt_pwrd__.bind("<Return>", self.__func_ok__)
        self.__txt_pwrd2__.bind("<Return>", self.__func_ok__)
        self.__btn_ok__.bind("<Return>", self.__func_ok__)
        self.__txt_usr__.focus()

    def __Check__(self, event=None):
        """Check if checkbutton's value is true or false to show or hide the password
and hide or show the password entry"""
        lst = "", "&"
        self.__txt_pwrd__.configure(show=lst[self.__var_check__.get()])
        if self.__var_check__.get() == 0:
            self.__frm2__.forget()
            self.__txt_pwrd__.focus()
            self.__txt_pwrd2__.destroy()
        else:
            self.__txt_pwrd2__ = self.__Entry__(self.__frm2__, width=15, show=self.__mask__)
            self.__txt_pwrd2__.grid(row=1, column=2)
            self.__txt_pwrd2__.focus()
            self.__txt_pwrd2__.bind("<Return>", self.__func_ok__)
            self.__frm2__.pack()
        self.__root__.update()

    def show(self):
        """show the login box and wait for the user's codes which would be return"""
        self.__root__.mainloop()
        return self.__usr__, self.__pwrd__

    def __cancel__(self, event=None):
        """Escape from the login-box"""
        self.__root__.destroy()

    def __error__(self, arg):
        """signal an error to the user"""
        from winsound import MessageBeep as snd
        snd(23)
        arg.configure(bg="red")
        arg.after(200, lambda col="SystemWindow": arg.configure(bg=col))
        arg.focus()
        pass

    def __func_ok__(self, event=None):
        """Central function which defines what to do"""
        from winsound import MessageBeep as snd
        self.__usr__, self.__pwrd__ = self.__txt_usr__.get(), self.__txt_pwrd__.get()
        pwrd2 = None
        try:
            pwrd2 = self.__txt_pwrd2__.get()
            self.__frm2__.info()
            show = True
        except:
            show = False
        if self.__usr__ == "":
            self.__error__(self.__txt_usr__)
        elif self.__pwrd__ == "":
            self.__error__(self.__txt_pwrd__)
        elif pwrd2 == "" and show == True:
            self.__error__(self.__txt_pwrd2__)
            pass
        elif pwrd2 != self.__pwrd__ and show == True:
            self.__txt_pwrd2__.destroy()
            self.__txt_pwrd2__ = self.__Entry__(self.__frm2__, width=15, show=self.__mask__)
            self.__txt_pwrd2__.grid(row=1, column=2)
            self.__txt_pwrd2__.focus()
            self.__txt_pwrd2__.bind("<Return>", self.__func_ok__)
            self.__txt_pwrd2__.after(750, self.__txt_pwrd2__.focus)
            popup(self.__root__, message="The 2 passwords are not\nthe sames please try again!")
        else:
            snd(75)
            self.__root__.destroy()

    def __reset__(self):
        """clear the user-name and the password"""
        try:
            self.__txt_usr__.destroy()
            self.__txt_pwrd__.destroy()
        except:
            pass
        try:
            self.__txt_usr__ = self.__Entry__(self.__frm__, width=15)
            self.__txt_usr__.grid(row=1, column=2)
            self.__txt_usr__.focus()
            self.__txt_pwrd__ = self.__Entry__(self.__frm__, width=15, show=self.__mask__)
            self.__txt_pwrd__.grid(row=2, column=2)
            self.__txt_usr__.bind("<Return>", self.__func_ok__)
            self.__txt_pwrd__.bind("<Return>", self.__func_ok__)
            self.__txt_usr__.focus()
        except:
            pass
        try:
            self.__root__.update()
        except:
            pass


class login2(login):
    """ classe dérivée de login,utile pour un accès à des comptes,données

options standards:
-title:le titre de la boite de dialogue(texte)
-mask:le caractère qui sera présenté pour cacher les lettre du mot de passe

options spéciales:

-func:la fonction qui prend en charge le nom utilisateur et le mot de passe saisient
elle doit retourner 'True' si ces derniers sont validés(reconnus) et 'False' si ils ne le
sont de manière à ce que la login box demande une nouvelle entrée!
            ex: def f(usr,pwrd):
                        db = dict(*usr,*pwrd)
                        if usr in db and db[usr] == pwrd:
                            return True
                        else:
                            return False
-func2act:la fonction qui se met en route une fois l'utilisateur reconnu elle doit accepter 2
arguments:
            ex: def f(usr,pwrd):
                    accès(usr)

-Nbre_essais:le nombre de fois qu'il sera demandé à l'utilisateur d'entrer ses infos

methodes /fonctions:
-show: affiche la boite de login et retourne les infos entrées par l'utilisateur
"""

    def __init__(self, func=None, func2act=None, title="Log into Box", Nbre_essais=3, mask="&"):
        """Contrucct a login-box"""
        login.__init__(self, title, mask)
        self.__remain__ = Nbre_essais
        self.__func__ = func
        self.__func2act__ = func2act
        self.__frm2__.destroy()

    def __Check__(self):
        """Check if checkbutton's value is true or false to show or hide the password"""
        lst = "", "&"
        self.__txt_pwrd__.configure(show=lst[self.__var_check__.get()])

    def __func_ok__(self, event=None):
        """Central function which defines what to do"""
        from winsound import MessageBeep as snd
        if self.__remain__ > 0:  ## If the chances are not all use
            self.__usr__, self.__pwrd__ = self.__txt_usr__.get(), self.__txt_pwrd__.get()
            if self.__usr__ == "":  ## If the User Name has been not entered
                self.__error__(self.__txt_usr__)
            elif self.__pwrd__ == "":  ## If the Password has been not entered
                self.__error__(self.__txt_pwrd__)
            else:  ## In different case:
                if self.__remain__ == 1:
                    self.__end__()
                if self.__func__ == None:
                    self.__root__.destroy()
                else:
                    ## Result is returned by "func" give at the instanciation of the login class,
                    ## and should be True or False
                    result = eval(str(self.__func__(self.__usr__, self.__pwrd__)))
                    if not result:  ## If the "func" funtion does not reconized the user-name and his password
                        self.__remain__ += -1
                        self.__reset__()
                        self.__txt_usr__.after(1000, self.__txt_usr__.focus)
                        popup(self.__root__, typ="warning")
                    else:  ## In case witch the "func" function reconize the user-name and his password
                        snd(60)
                        self.__func2act__(self.__usr__, self.__pwrd__)
                        self.__root__.destroy()


        else:
            self.__root__.destroy()
            popup(message="You havent log in please try later!", delai=2000)

    def __end__(self, event=None):
        """close/destroy the login-box"""
        self.__root__.after(50, self.__root__.destroy)

    def show(self):
        """ Show the login-box and wait for user'entries"""
        self.__root__.mainloop()
        if self.__func__ == None:
            return self.__usr__, self.__pwrd__


            ################
            ## Testing Code  ##
            ################


if __name__ == "__main__":
    db = dict((("Franck Mario", "spy_anf"), ("Chimene", "Deco"), ("Samy", "118"), ("Nathan", "117")))


    def f(usr, pswrd):
        if usr in db and db[usr] == pswrd:
            print(" C'est how " + usr + " ça fait plutôt longueur!")
            return True
        else:
            print("Je ne te connais/reconnais pas/plus")
            return False


    code = login2(f, f)
    me = code.show()
