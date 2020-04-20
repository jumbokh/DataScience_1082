def main():
    keywords = {'and', 'del', 'or', 'not', 'while',     
                'for', 'with', 'break', 'True', 'False'    
                'elif', 'else', 'if', 'break', 'except',
                'import', 'print', 'class', 'in'             
                'continue', 'finally', 'is', 'return',              
                'def', 'try'}

    f1 = input('Enter a Python source code filename: ').strip()

    # Open files for input 
    infile = open(f1, 'r')
    
    text = infile.read().split()
    
    count = 0
    for word in text: 
        if word in keywords:
            count += 1
    
    print('There are %d keywords in %s'%(count, f1))
    
main()