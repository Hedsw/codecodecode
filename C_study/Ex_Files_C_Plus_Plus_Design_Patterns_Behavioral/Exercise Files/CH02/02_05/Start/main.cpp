//
//  main.cpp
//  command-pattern
//

#include <iostream>
#include <vector>

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

class Command {
    public:
        virtual ~Command() {};
        virtual void execute() = 0;
};

class Button {
    Command * command;
    public:
        Button(Command * command) : command(command) {};
        void click() {
            command->execute();
        }
};

class AddShapeCommand: public Command { 
    std::string ShapeName;
    Canvas *canvas;
    public: 
        AddShapeCommand(const std::string & shapeName, Canvas * canvas) :
            ShapeName(shapeName), canvas(canvas) {};

    void execute() {
        canvas->addShape(ShapeName);
    }
};

class ClearCommand: public Command {
    Canvas * canvas;
    public:
        ClearCommand(Canvas *canvas) : canvas(canvas) {};
        void execute() {
            canvas->clearAll();
        }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
