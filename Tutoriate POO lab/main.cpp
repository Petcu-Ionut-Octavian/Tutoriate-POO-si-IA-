#include <iostream>

/*========================================================
  EXEMPLUL 1 - OVERLOADING DUPĂ TIPUL PARAMETRILOR
========================================================*/

class Calculator1 {
public:
    void afiseaza(int x) {
        std::cout << "int: " << x << '\n';
    }

    void afiseaza(double x) {
        std::cout << "double: " << x << '\n';
    }

    void afiseaza(char x) {
        std::cout << "char: " << x << '\n';
    }
};

void ex1_overloading_tip() {
    Calculator1 c;

    c.afiseaza(10);
    c.afiseaza(3.14);
    c.afiseaza('A');
}

/*========================================================
  EXEMPLUL 2 - OVERLOADING DUPĂ NUMĂRUL PARAMETRILOR
========================================================*/

class Calculator2 {
public:
    int suma(int a, int b) {
        return a + b;
    }

    int suma(int a, int b, int c) {
        return a + b + c;
    }
};

void ex2_overloading_numar_parametri() {
    Calculator2 c;

    std::cout << c.suma(2, 3) << '\n';
    std::cout << c.suma(2, 3, 4) << '\n';
}

/*========================================================
  EXEMPLUL 3 - OVERLOADING DUPĂ ORDINE
========================================================*/

class Exemplu3 {
public:
    void f(int x, double y) {
        std::cout << "int, double\n";
    }

    void f(double x, int y) {
        std::cout << "double, int\n";
    }
};

void ex3_overloading_ordine() {
    Exemplu3 obj;

    obj.f(10, 3.14);
    obj.f(3.14, 10);
}

/*========================================================
  EXEMPLUL 4 - HIDING
========================================================*/

class B1 {
public:
    void f() {
        std::cout << "B1::f()\n";
    }
};

class D1 : public B1 {
public:
    void f(int x) {
        std::cout << "D1::f(" << x << ")\n";
    }
};

void ex4_hiding() {
    D1 d;

    d.f(10);

    // d.f(); // eroare
}

/*========================================================
  EXEMPLUL 5 - REZOLVAREA HIDING-ULUI
========================================================*/

class B2 {
public:
    void f() {
        std::cout << "B2::f()\n";
    }
};

class D2 : public B2 {
public:
    void f(int x) {
        std::cout << "D2::f(" << x << ")\n";
    }
};

void ex5_rezolvare_hiding() {
    D2 d;

    d.B2::f();
    d.f(10);
}

/*========================================================
  EXEMPLUL 6 - OVERRIDING
========================================================*/

class Animal {
public:
    void sunet() {
        std::cout << "Sunet generic\n";
    }
};

class Dog : public Animal {
public:
    void sunet() {
        std::cout << "Ham Ham\n";
    }
};

void ex6_overriding() {
    Dog d;

    d.sunet();
}

/*========================================================
  EXEMPLUL 7 - ACCESAREA METODEI SUPRASCRISE
========================================================*/

class Persoana {
public:
    void prezentare() {
        std::cout << "Persoana\n";
    }
};

class Student : public Persoana {
public:
    void prezentare() {
        std::cout << "Student\n";
    }
};

void ex7_metoda_suprascrisa() {
    Student s;

    s.prezentare();
    s.Persoana::prezentare();
}

/*========================================================
  EXEMPLUL 8 - OPERATORUL ::
========================================================*/

class B3 {
public:
    void f() {
        std::cout << "B3::f()\n";
    }
};

class D3 : public B3 {
public:
    void f() {
        std::cout << "D3::f()\n";
    }
};

void ex8_rezolutie() {
    D3 d;

    d.f();
    d.B3::f();
}

/*========================================================
  EXEMPLUL 9 - UPCASTING CU POINTER
========================================================*/

class Shape {
};

class Circle : public Shape {
};

void ex9_upcasting_pointer() {
    Circle c;

    Shape* p = &c;

    (void)p;

    std::cout << "Upcasting realizat\n";
}

/*========================================================
  EXEMPLUL 10 - UPCASTING CU REFERINTA
========================================================*/

class Shape2 {
};

class Circle2 : public Shape2 {
};

void ex10_upcasting_referinta() {
    Circle2 c;

    Shape2& ref = c;

    (void)ref;

    std::cout << "Upcasting prin referinta\n";
}

/*========================================================
  EXEMPLUL 11 - TABLOU POLIMORFIC
========================================================*/

class Shape3 {
};

class Circle3 : public Shape3 {
};

class Square3 : public Shape3 {
};

void ex11_tablou_pointeri() {
    Shape3* forme[2];

    forme[0] = new Circle3();
    forme[1] = new Square3();

    std::cout << "Tablou de Shape*\n";

    delete forme[0];
    delete forme[1];
}

/*========================================================
  EXEMPLUL 12 - LIMITAREA UPCASTING-ULUI
========================================================*/

class Shape4 {
public:
    void draw() {
        std::cout << "Draw\n";
    }
};

class Circle4 : public Shape4 {
public:
    void setRadius() {
        std::cout << "Radius\n";
    }
};

void ex12_limitari_upcasting() {
    Circle4 c;

    Shape4* p = &c;

    p->draw();

    // p->setRadius(); // eroare
}

/*========================================================
  EXEMPLUL 13 - DOWNCASTING
========================================================*/

class Shape5 {
public:
    virtual ~Shape5() = default;
};

class Circle5 : public Shape5 {
public:
    void info() {
        std::cout << "Circle5\n";
    }
};

void ex13_downcasting() {
    Shape5* p = new Circle5();

    Circle5* c =
        static_cast<Circle5*>(p);

    c->info();



    delete p;
}

/*========================================================
  MAIN
========================================================*/

int main() {

    // ex1_overloading_tip();

    // ex2_overloading_numar_parametri();

    // ex3_overloading_ordine();

    // ex4_hiding();

    // ex5_rezolvare_hiding();

    // ex6_overriding();

    // ex7_metoda_suprascrisa();

    // ex8_rezolutie();

    // ex9_upcasting_pointer();

    // ex10_upcasting_referinta();

    // ex11_tablou_pointeri();

    // ex12_limitari_upcasting();

    // ex13_downcasting();

    return 0;
}