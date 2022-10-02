// 04_04_AbFacRun_Start.cpp : 
#include <iostream>
#define strcpy_s strcpy
using namespace std;

//Door Objects
class Door
{
public:
	Door()
	{
	}
	virtual void Open() = 0;
};

class GasCarDoor : public Door
{
public:
	GasCarDoor()
	{
		cout << "Making a door for a gas car." << endl;
	}
	void Open()
	{
		cout << "click" << endl;
	}
};

class ElectricCarDoor : public Door
{
public:
	ElectricCarDoor()
	{
		cout << "Making a door for an electric car" << endl;
	}
	void Open()
	{
		cout << "shhhhh" << endl;
	}
};

//Engine objects
class Engine
{
protected:
	char _sound[15];
public:
	Engine()
	{
		strcpy_s(_sound, "");
	}
	virtual void Run() = 0;
};

class GasEngine : public Engine
{
public:
	GasEngine()
	{
		strcpy_s(_sound, "vroom");
		cout << "Making a gas engine." << endl;
	}
	void Run()
	{
		cout << _sound << endl;
	}
};

class ElectricEngine : public Engine
{
public:
	ElectricEngine()
	{
		strcpy_s(_sound, "SHHHH");
		cout << "Making an electric engine." << endl;
	}
	void Run()
	{
		cout << _sound << endl;
	}
};

//Factories
class CarFactory
{
public:
	virtual Door* BuildDoor() = 0;
	virtual Engine* BuildEngine() = 0;
};

class GasCarFactory :public CarFactory
{
public:
	Door * BuildDoor()
	{
		return new GasCarDoor();
	}
	Engine* BuildEngine()
	{
		return new GasEngine();
	}
};

class ElectricCarFactory :public CarFactory
{
public:
	Door * BuildDoor()
	{
		return new ElectricCarDoor();
	}
	Engine* BuildEngine()
	{
		return new ElectricEngine();
	}
};

int main()
{
	CarFactory* CarPlant;
	int choice;

	cout << "Select a car type: " << endl;
	cout << "1: Gasoline" << endl;
	cout << "2: Electric" << endl;
	cout << "Selection: ";
	cin >> choice;
	cout << endl;

	switch (choice)
	{
	case 1:
		CarPlant = new GasCarFactory;
		break;
	case 2:
		CarPlant = new ElectricCarFactory;
		break;
	default:
		cout << "Invalid Selection" << endl;
		CarPlant = NULL;
		break;
	}

	if (CarPlant != NULL)
	{
		Door* myDoor = CarPlant->BuildDoor();
		Engine* myEngine = CarPlant->BuildEngine();

		myDoor->Open();
		myEngine->Run();
	}
}