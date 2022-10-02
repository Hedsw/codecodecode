#include <iostream>
using namespace std;

class Background {
    public:
    Background() {

    }
    virtual void color() = 0;
};

class DarkColor : public Background {
    public:
    DarkColor() {
        cout << " Making Background color to Dark color " << endl;
    }

    void color() {
        cout << "Dark Background Color" << endl;
    }
};

class WhiteColor: public Background {
    public:
    WhiteColor() {
        cout << "Making Background color to White Color" << endl;
    }

    void color() {
        cout << "White Background Color" << endl;
    }
};

class TextColor {
    public:
    TextColor() {

    }
    virtual void _textcolor() = 0;
};

class WhiteText : public TextColor {
    public:
    WhiteText() {
        cout << "Making Textcolor to white Color" << endl;
    }

    void _textcolor() {
        cout << "White Textcolor" << endl;
    }
};

class BlackText : public TextColor {
    public:
    BlackText() {
        cout << "Making Textcolot to Black Color" << endl;
    }

    void _textcolor() {
        cout << "Black Text Color" << endl;
    }
};

class BackgroundFactory {
    public:
    virtual TextColor* changecolor() = 0;
    virtual Background* backgroundColor() = 0;
};

class DarkFactory : public BackgroundFactory {
    public:
    TextColor * changecolor() {
        return new BlackText();
    }
    
    Background * backgroundColor() {
        return new DarkColor();
    }
};

class WhiteFactory: public BackgroundFactory {
    public:
    TextColor* changecolor() {
        return new WhiteText();
    }
    Background* backgroundColor() {
        return new WhiteColor(); 
    }
};

int main() {
    BackgroundFactory* BFactory;
    int choice;

    cout << "Select a car type: " << endl;
	cout << "1: Background" << endl;
	cout << "2: Text" << endl;
	cout << "Selection: ";
	cin >> choice;
	cout << endl;

    switch (choice)
	{
	case 1: // Black
		BFactory = new DarkFactory;
		break;
	case 2: // White
		BFactory = new WhiteFactory;
		break;
	default:
		cout << "Invalid Selection" << endl;
		BFactory = NULL;
		break;
	}

    if (BFactory != NULL) {
        Background* myBackground = BFactory->backgroundColor();
        TextColor* myTextColor = BFactory->changecolor();

        myBackground->color();
        myTextColor->_textcolor();
    }
}
