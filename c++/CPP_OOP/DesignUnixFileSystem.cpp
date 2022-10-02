/*
You are asked to design a file system that allows you to create new paths and associate 
them with different values.
The format of a path is one or more concatenated strings of the form: 
/ followed by one or more lowercase English letters. For example, "/leetcode" 
and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:
bool createPath(string path, int value) Creates a new path and associates 
a value to it if possible and returns true. Returns false if the path already exists 
or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1
 if the path doesn't exist.
*/

// Time complexity - O(N)
// Space Complexity -(1)
struct TrieNode {
    unordered_map<string, TrieNode*> child;
    bool isFile;
    int content;
    
    TrieNode() {
        isFile = false;
        content = -1;
    }
};

class FileSystem {
private:
    TrieNode* root = nullptr;
    
    vector<string> split(string& path) {
        vector<string> result;
        string cur = "";
        for(int i = 1; i < path.size(); ++i) {
            char c = path[i];
            if (c== '/') {
                result.push_back(cur);
                cur = "";
            }
            else {
                cur.push_back(c);
            }
        }
        result.push_back(cur);
        return result;
    }
    
    bool insert(vector<string>& path, int value) {
        int n = path.size();
        TrieNode* cur = root;
        for (int i = 0; i < n; ++i) {
            if (cur -> child.find(path[i]) == cur -> child.end()) {
                if( i != n - 1) {
                    return false;
                }
                cur -> child[path[i]] = new TrieNode();
            }
            else {
                if (i == n - 1) {
                    return false; // the path already exist 
                }
            }
            cur = cur -> child[path[i]];
        }
        cur -> isFile = true;
        cur -> content = value;
        return true;
    }
    
    int find(vector<string> path) {
        int n = path.size();
        TrieNode* cur = root;
        for (int i = 0; i < n; ++i) {
            if (cur -> child.find(path[i]) == cur -> child.end()) {
                return -1;
            }
            
            cur = cur -> child[path[i]];
        }
        return cur -> content;
    }
    
public:
    FileSystem() {
        root = new TrieNode();
    }
    
    bool createPath(string path, int value) {
        vector<string> p = split(path);
        return insert(p, value);
    }
    
    int get(string path) {
        vector<string> p = split(path);
        return find(p);
    }
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * bool param_1 = obj->createPath(path,value);
 * int param_2 = obj->get(path);
 */