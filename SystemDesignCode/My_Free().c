void my_free(int address)
{
    int i =0;
    int copy_meta_data = FALSE;
    
    for(i = 0; i < g_allocted_number; i++)
    {
        if(address == metadata_info[i].address)
        {
            // memset(&our_memory[metadata_info[i].address], 0, metadata_info[i].size);
            g_allocted_number -= 1;
            copy_meta_data = TRUE;
            printf("g_allocted_number in free = %d %d\n", g_allocted_number, address);
            break;
        }
    }
    // Test it
    // Copy meta data
    if(copy_meta_data == TRUE)
    {
        if(i == MAX_ALOCATION_ALLOWED -1)
        {
            metadata_info[i].address = 0;
            metadata_info[i].size = 0;
        }
        else
            memcpy(&metadata_info[i], &metadata_info[i+1], sizeof(malloc_info_t));
    }
}