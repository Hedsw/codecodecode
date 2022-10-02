//
//  main.cpp
//  command-pattern
//
//

#include <iostream>
#include <vector>

class Command {
public:
    virtual ~Command() {};
    virtual void execute() = 0;
};

class Canvas {
    std::vector<std::string> shapes;
public:
    void addShape(const std::string & newShape) {
        shapes.push_back(newShape);
    };
    void clearAll() {
        shapes.clear();
    };
    std::vector<std::string> getShapes() { return shapes; };
};

class Button {
public:
    virtual ~Button() {};
    virtual void click() = 0;
};

class AddShapeCommand: public Command {
    std::string shapeName;
    Canvas *canvas;
public:
    AddShapeCommand(const std::string & shapeName, Canvas* canvas) : shapeName(shapeName), canvas(canvas) {};
    void execute() {
        canvas->addShape(shapeName);
    }
};

class ClearCommand: public Command {
    Canvas *canvas;
public:
    ClearCommand(Canvas *canvas) : canvas(canvas) {};
    void execute() {
        canvas->clearAll();
    }
};

class AddTriangleButton : public Button {
    Canvas *canvas;
public:
    AddTriangleButton(Canvas *canvas) : canvas(canvas) {};
    void click() override {
        canvas->addShape("triangle");
    }
};

class AddSquareButton : public Button {
    Canvas *canvas;
public:
    AddSquareButton(Canvas *canvas) : canvas(canvas) {};
    void click() override {
        canvas->addShape("square");
    }
};

class ClearButton : public Button {
    Canvas *canvas;
public:
    ClearButton(Canvas *canvas) : canvas(canvas) {};
    void click() override {
        canvas->clearAll();
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
