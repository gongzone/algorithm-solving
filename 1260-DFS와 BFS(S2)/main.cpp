#include <iostream>
#include <list>
#include <stack>
#include <queue>

int v_num;
int e_num;
int starting;

class Graph
{
private:
    int V;
    bool *visited;
    std::list<int> *adj;
    std::list<int>::iterator iter;

public:
    Graph(int V);
    ~Graph();
    void addEdge(int x, int y);
    void adjSort();
    void BFS(int starting);
    void DFS(int starting);
};

Graph::Graph(int V)
{
    this->V = V;
    visited = new bool[V];
    adj = new std::list<int>[V];
}

Graph::~Graph()
{
    delete []visited;
    delete []adj;
}

void Graph::addEdge(int x, int y)
{
    adj[x].push_back(y);
}

void Graph::DFS(int starting)
{
    for(int i = 1; i < V; i++)
        visited[i] = false;

    for(int i = 1; i < V; i++)
        adj[i].sort(std::greater<int>());

    std::stack<int> s;

    s.push(starting);

    while(!s.empty())
    {
        starting = s.top();
        s.pop();

        if(!visited[starting])
        {
            std::cout << starting << " ";
            visited[starting] = true;
        }
        else
            continue;

        for(iter = adj[starting].begin(); iter != adj[starting].end(); iter++)
        {
            if(!visited[*iter])
                s.push(*iter);
        }
    }

    std::cout << "\n";
}

void Graph::BFS(int starting)
{
    for(int i = 1; i < V; i++)
        visited[i] = false;

    for(int i = 1; i < V; i++)
        adj[i].sort();

    std::queue<int> q;

    visited[starting] = true;
    q.push(starting);

    while(!q.empty())
    {
        starting = q.front();
        std::cout << starting << " ";
        q.pop();

        for(iter = adj[starting].begin(); iter != adj[starting].end(); iter++)
        {
            if(!visited[*iter])
            {
                visited[*iter] = true;
                q.push(*iter);
            }
        }
    }

    std::cout << "\n";
}


int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::cin >> v_num >> e_num >> starting;

    Graph g(v_num + 1);

    int x;
    int y;

    while(e_num--)
    {
        std::cin >> x >> y;
        g.addEdge(x, y);
        g.addEdge(y, x);
    }

    g.DFS(starting);
    g.BFS(starting);

    return 0;
}
