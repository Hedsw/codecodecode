// 06_02_ProtoSetUp_Start.cpp 
#include <iostream>
using namespace std;

// Abstract Animal class
class Animal
{
protected:
	char _hairColor[10];
	int _hairLength, _tail, _weight, _height, _age;
	int _intelligence, _stubbornness, _agressiveness;

public:
	virtual Animal  *clone() = 0;

	int setHairLength(int length)
	{
		_hairLength = length;
	}

	void setHairColor(const char *color)
	{
		strcpy_s(_hairColor, color);
	}

	void setTail(int length)
	{
		_tail = length;
	}

	void setWeight(int kg)
	{
		_weight = kg;
	}

	void setHeight(int m)
	{
		_height = m;
	}

	void setAge(int age)
	{
		_age = age;
	}

};

// Derived Sheep class
class Sheep : public Animal
{
public:
	Sheep()
	{
		_hairLength = 5;
		_stubbornness = 3;
		_agressiveness = 2;
		_intelligence = 7;
	}
	sheep* clone() {
		return new Sheep(*this);
	}
	void sharing() {
		_hairLength = _hairLength - 2;
	}
};

// Derived Cow class
class Cow : public Animal
{
public:
	Cow()
	{
		_stubbornness = 6;
		_agressiveness = 5;
		_intelligence = 8;
	}

	Cow* clone() {
		return new Cow(*this);
	}

	void sharing() {
		_hairLength = _hairLength - 3;
	}

};

int main()
{
	//create initial instance of a Sheep
	Sheep * sheep0 = new Sheep;
	sheep0->setHairColor("white");
	sheep0->setTail(5);
	sheep0->setWeight(90);
	sheep0->setHeight(1);
	sheep0->setAge(5);
	
	//create initial instance of a Cow
	Cow * cow0 = new Cow;
	cow0->setHairColor("Brown");
	cow0->setTail(20);
	cow0->setWeight(90);
	cow0->setHeight(1);
	cow0->setAge(8);

	Animal *farm[3];
	
	//use cloning to populate the farm
	farm[0] = sheep0->clone();
	farm[1] = cow0->clone();
	// farm[2] = 

	//change a cow property
	farm[1]->setWeight(1000);

	//shear a Sheep and clone it
	sheep0->sharing();
	farm[2] = sheep0->clone();


}

