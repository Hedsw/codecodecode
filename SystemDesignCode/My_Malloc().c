#define TRUE        1
#define FALSE       0

#define MAX_ALOCATION_ALLOWED       20
static unsigned char our_memory[1024 * 1024];

static int g_allocted_number = 0;
static int g_heap_base_address = 0;

typedef struct malloc_info
{
    int address;
    int size;
}malloc_info_t;

malloc_info_t   metadata_info[MAX_ALOCATION_ALLOWED] ={0};

void* my_malloc(int size)
{
    int j =0;
    int index = 0 ;
    int initial_gap =0;
    int gap =0;
    int flag = FALSE;
    int initial_flag = FALSE;
    void *address = NULL;
    int heap_index = 0;
    malloc_info_t temp_info = {0};

    if(g_allocted_number >= MAX_ALOCATION_ALLOWED)
    {
        return NULL;
    }

    for(index = 0; index < g_allocted_number; index++)
    {
        if(metadata_info[index+1].address != 0 )
        {
            initial_gap = metadata_info[0].address - g_heap_base_address; /*Checked Initial Block (Case 3)*/
            if(initial_gap >= size)
            {
                initial_flag = TRUE;
                break;
            }
            else
            {
                gap = metadata_info[index+1].address - (metadata_info[index].address + metadata_info[index].size);  /*Check Gap Between two allocated memory (Case 2)*/
                if(gap >= size)
                {
                    flag = TRUE;
                    break;
                }
            }
        }
    }

    if(flag == TRUE)    /*Get Index for allocating memory for case 2*/
    {
        heap_index = ((metadata_info[index].address + metadata_info[index].size) - g_heap_base_address);
    
        for(j = MAX_ALOCATION_ALLOWED -1; j > index+1; j--)
        {
            memcpy(&metadata_info[j], &metadata_info[j-1], sizeof(malloc_info_t));
        }
    }
    else if (initial_flag == TRUE) /*Get Index for allocating memory for case 3*/
    {
        heap_index = 0;
        for(j = MAX_ALOCATION_ALLOWED -1; j > index+1; j--)
        {
            memcpy(&metadata_info[j], &metadata_info[j-1], sizeof(malloc_info_t));
        }
    }
    else /*Get Index for allocating memory for case 1*/
    {
        if(g_allocted_number != 0)
        {
            heap_index = ((metadata_info[index -1].address + metadata_info[index-1].size) - g_heap_base_address);
        }
        else    /* 0 th Location of Metadata for First time allocation*/
            heap_index = 0;
    }

    address = &our_memory[heap_index];
    metadata_info[index].address = g_heap_base_address + heap_index;
    metadata_info[index].size = size;

    g_allocted_number += 1;
    return address;
}