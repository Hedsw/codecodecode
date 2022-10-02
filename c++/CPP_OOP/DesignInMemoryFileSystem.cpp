/* 
Trie + unordered_map 조합으로 품 

n = depth(path), m = size(content)
Time Comp: 
ls: O(n)
mkdir: O(n)
addContentToFile: O(n+m)
readContentFromFile: O(n)

Space Comp:
ls: O(n)
mkdir: O(n)
addContentToFile: O(n+m)
readContentFromFile: O(n)

Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]
*/
struct Node {        
    unordered_map<string, Node *> dir = {};
    vector<string> pathList = {};
    string content = "";    
};

class FileSystem {
private:
    Node *main;
public:
    FileSystem() {
        main = new Node;
    }
    
    vector<string> ls(string path) {     
        Node *temp = file(path);
        if (temp->content.size())
            return {path.substr(path.find_last_of('/') + 1)};
        sort(temp->pathList.begin(), temp->pathList.end());
        return temp->pathList;
    }
    
    void mkdir(string path) {
        file(path);
    }
    
    void addContentToFile(string filePath, string content) {
        Node *temp = file(filePath);
        temp->content += content;  
    }
    
    string readContentFromFile(string filePath) {
        Node *temp = file(filePath);
        return temp->content;
    }
    
    Node *file(string path) {
        Node *temp = main;
        stringstream ss(path);
        string currPath = "";
        
        while (getline(ss, currPath, '/')) {
            // If the file does not exist
            if (temp->dir[currPath] == nullptr) {
                temp->pathList.push_back(currPath);                
                temp->dir[currPath] = new Node;
            }
            temp = temp->dir[currPath];                
        }
        return temp;
    }
};
/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * vector<string> param_1 = obj->ls(path);
 * obj->mkdir(path);
 * obj->addContentToFile(filePath,content);
 * string param_4 = obj->readContentFromFile(filePath);
 */