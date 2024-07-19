// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26 * 26 * 26;
unsigned int counter = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_index = hash(word);
    // Iteration through the linked list of the table's hash_index
    node *cursor = table[hash_index];
    while (cursor)
    {
        if (strcasecmp(word, cursor->word) == 0)
            return true;
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (word == NULL || word[0] == '\0' || word[1] == '\0' || word[2] == '\0')
        return 0;

    // Get the indices of the first three letters, not considering their case.
    unsigned first_index = toupper(word[0]) - 'A';
    unsigned second_index = toupper(word[1]) - 'A';
    unsigned third_index = toupper(word[2]) - 'A';

    // Making sure that the indices are not out of range [0, 25].
    first_index %= 26;
    second_index %= 26;
    third_index %= 26;

    // Combine the three indices into a single hash value.
    unsigned int hash_index = (first_index * 26 * 26) + (second_index * 26) + third_index;

    return (hash_index);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dictionary file
    FILE *infile = fopen(dictionary, "r");
    if (!infile)
        return false;

    // Declare a buffer to read one word at a time

    char buffer[LENGTH + 1];

    // Scan words until EOF
    while (fscanf(infile, "%s", buffer) != EOF)
    {
        // Create a new node
        node *new_node = malloc(sizeof(node));
        if (!new_node)
            return false;

        strcpy(new_node->word, buffer);

        int hash_index = hash(new_node->word);

        if (table[hash_index] == NULL)
            new_node->next = NULL;

        else
            new_node->next = table[hash_index];
        table[hash_index] = new_node;

        counter++;
    }
    fclose(infile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}

