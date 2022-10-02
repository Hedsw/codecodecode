#include <string>
#include <vector>
#include <iostream>
#include <unordered_set>

#include <assert.h>

using namespace std;

/*
Decorator Pattern 사용함
Decorator is a structural pattern that allows adding new behaviors to objects dynamically
 by placing them inside special wrapper objects, called decorators.
*/

class Rule
{
private:
    unordered_set<string> words;

public:
    virtual string valid(string s) = 0;

    unordered_set<string> getWords()
    {
        return words;
    }

    void addWord(string word)
    {
        words.insert(word);
    }

    bool match(string c)
    {
        return words.count(c) == 1;
    }

    vector<string> split(string str, string pattern)
    {
        string::size_type pos;
        vector<std::string> result;
        str += pattern;
        int size = str.size();

        for (int i = 0; i < size; i++)
        {
            pos = str.find(pattern, i);
            if (pos < size)
            {
                std::string s = str.substr(i, pos - i);
                result.push_back(s);
                i = pos + pattern.size() - 1;
            }
        }
        return result;
    }
};

class AdRule : public Rule
{
public:
    string valid(string s)
    {
        string r = "";
        auto words = split(s, " ");

        for (auto word : words)
        {
            if (!match(word))
            {
                r = r + " " + word;
            }
            else
            {
                r += " *";
            }
        }
        return r;
    }
};

class PornRule : public Rule
{
public:
    string valid(string s)
    {
        string r = "";
        auto words = split(s, " ");
        for (auto word : words)
        {
            if (match(word))
            {
                return "";
            }
            else
            {
                r = r + " " + word;
            }
        }
        return r;
    }
};

class Filter
{
private:
    vector<Rule *> rules;

public:
    void addRule(Rule *rule)
    {
        rules.push_back(rule);
    }

    string valid(string s)
    {
        for (Rule *rule : rules)
        {
            s = rule->valid(s);
        }

        return s;
    }
};

class Comment
{
private:
    string content;
    Filter *filter;

public:
    Comment(string s, Filter *f) : content(s), filter(f)
    {
    }

    string valid()
    {
        return filter->valid(content);
    }
};

int main()
{
    AdRule *adRule = new AdRule();
    adRule->addWord("ad");
    adRule->addWord("buy");

    PornRule *pornRule = new PornRule();
    pornRule->addWord("porn");
    pornRule->addWord("sex");

    Filter *filter = new Filter();
    filter->addRule(adRule);
    filter->addRule(pornRule);

    Comment *c1 = new Comment("this is a ad", filter);
    assert(c1->valid() == "  this is a *");

    Comment *c2 = new Comment("this is a porn", filter);
    assert(c2->valid() == "");

    return 0;
}