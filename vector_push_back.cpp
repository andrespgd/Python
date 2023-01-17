#include <iostream>
#include <vector>

int main()
{ 
    std::vector<int> vector1 = {0,1,2,3,4,5};

    std::cout<<"\n vector1"<<std::endl; 
    for (int i=0; i<vector1.size();i++)
    {
        std::cout<<"i="<<i<<","<<vector1[i]<<std::endl;
    }
    
    vector1.push_back(6);
    
    std::cout<<"\n vector1 + push_back(6)"<<std::endl;  
    for (int i=0; i<vector1.size();i++)
    {
        std::cout<<"i="<<i<<","<<vector1[i]<<std::endl;
    }   
    
    return 0;
}
