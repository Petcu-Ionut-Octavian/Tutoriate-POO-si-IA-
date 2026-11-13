#include <iostream>

/*========================================================
  EXEMPLUL 1 - IS A (moștenire simplă)
========================================================*/

class Animal {
public:
    void mananca() const {
        std::cout << "Animalul mananca\n";
    }
};

class Dog : public Animal {
};

void ex1_mostenire_simpla() {
    Dog d;
    d.mananca();
}

/*========================================================
  EXEMPLUL 2 - HAS A (compunere)
========================================================*/

class Motor {
public:
    void porneste() const {
        std::cout << "Motor pornit\n";
    }
};

class Masina {
private:
    Motor motor;

public:
    void pornesteMasina() {
        motor.porneste();
    }
};

void ex2_compunere() {
    Masina m;
    m.pornesteMasina();
}

/*========================================================
  EXEMPLUL 3 - MOȘTENIRE PUBLICĂ
========================================================*/

class A1 {
public:
    int x = 10;

protected:
    int y = 20;
};

class B1 : public A1 {
public:
    void afisare() const {
        std::cout << x << ' ' << y << '\n';
    }
};

void ex3_public_inheritance() {
    B1 obj;
    obj.afisare();
}

/*========================================================
  EXEMPLUL 4 - MEMBRI PRIVATE
========================================================*/

class Animal2 {
private:
    int varsta = 5;

public:
    int getVarsta() const {
        return varsta;
    }
};

class Dog2 : public Animal2 {
};

void ex4_private_members() {
    Dog2 d;

    // d.varsta; // eroare

    std::cout << d.getVarsta() << '\n';
}

/*========================================================
  EXEMPLUL 5 - ORDINEA CONSTRUCTORILOR
========================================================*/

class A2 {
public:
    A2() {
        std::cout << "Constructor A2\n";
    }
};

class B2 : public A2 {
public:
    B2() {
        std::cout << "Constructor B2\n";
    }
};

void ex5_constructori() {
    B2 obj;
}

/*========================================================
  EXEMPLUL 6 - ORDINEA DESTRUCTORILOR
========================================================*/

class A3 {
public:
    A3() {
        std::cout << "A3 construit\n";
    }

    ~A3() {
        std::cout << "A3 distrus\n";
    }
};

class B3 : public A3 {
public:
    B3() {
        std::cout << "B3 construit\n";
    }

    ~B3() {
        std::cout << "B3 distrus\n";
    }
};

void ex6_destructori() {
    B3 obj;
}

/*========================================================
  EXEMPLUL 7 - CONSTRUCTOR PARAMETRIZAT ÎN BAZĂ
========================================================*/

class A4 {
public:
    explicit A4(int x) {
        std::cout << "A4 = " << x << '\n';
    }
};

class B4 : public A4 {
public:
    B4()
        : A4(100) {
        std::cout << "Constructor B4\n";
    }
};

void ex7_constructor_parametrizat() {
    B4 obj;
}

/*========================================================
  EXEMPLUL 8 - LANȚ DE MOȘTENIRE
========================================================*/

class A5 {
public:
    A5() {
        std::cout << "A5\n";
    }
};

class B5 : public A5 {
public:
    B5() {
        std::cout << "B5\n";
    }
};

class C5 : public B5 {
public:
    C5() {
        std::cout << "C5\n";
    }
};

void ex8_lant_mostenire() {
    C5 obj;
}

/*========================================================
  EXEMPLUL 9 - MOȘTENIRE MULTIPLĂ
========================================================*/

class Student {
public:
    Student() {
        std::cout << "Constructor Student\n";
    }
};

class Angajat {
public:
    Angajat() {
        std::cout << "Constructor Angajat\n";
    }
};

class Asistent : public Student, public Angajat {
public:
    Asistent() {
        std::cout << "Constructor Asistent\n";
    }
};

void ex9_mostenire_multipla() {
    Asistent a;
}

/*========================================================
  EXEMPLUL 10 - AMBIGUITATE
========================================================*/

class A6 {
public:
    void f() const {
        std::cout << "A6::f\n";
    }
};

class B6 {
public:
    void f() const {
        std::cout << "B6::f\n";
    }
};

class C6 : public A6, public B6 {
};

void ex10_ambiguitate() {
    C6 obj;

    obj.A6::f();
    obj.B6::f();
}

/*========================================================
  EXEMPLUL 11 - IS A vs HAS A
========================================================*/

class Persoana {
};

class Student2 : public Persoana {
};

class Facultate {
private:
    Student2 student;
};

void ex11_isa_hasa() {
    std::cout << "Student2 IS A Persoana\n";
    std::cout << "Facultate HAS A Student2\n";
}

/*========================================================
  MAIN
========================================================*/

int main() {
    //
    // ex1_mostenire_simpla();
    //
    // ex2_compunere();
    //
    // ex3_public_inheritance();
    //
    // ex4_private_members();
    //
    // ex5_constructori();
    //
    // ex6_destructori();
    //
    // ex7_constructor_parametrizat();
    //
    // ex8_lant_mostenire();
    //
    // ex9_mostenire_multipla();
    //
    // ex10_ambiguitate();
    //
    // ex11_isa_hasa();

    return 0;
}