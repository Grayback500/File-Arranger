#include <algorithm>
#include <boost/filesystem/directory.hpp>
#include <boost/filesystem/file_status.hpp>
#include <boost/filesystem/operations.hpp>
#include <cctype>
#include <cstddef>
#include <iostream>
#include <map>
#include <string>
#include <boost/filesystem.hpp>
#include <ncurses.h>
#include <stdlib.h>

namespace fs = boost::filesystem;
using namespace std;

// Function declarations
string expandUser(string &END_PATH);
void fileArranger();
void terminalOutput();

// GLOBAL VARIABLES
string DOWNLOADS_PATH = expandUser("~/Downloads");
// create map of folder paths for each file type
map<string, string> FOLDER_EXT_PATHS = {
  {"mp3", DOWNLOADS_PATH + "/Music"},
  {"m4a", DOWNLOADS_PATH + "/Music"},
  {"png", DOWNLOADS_PATH + "/Pictures"},
  {"jpeg", DOWNLOADS_PATH + "/Pictures"},
  {"gif", DOWNLOADS_PATH + "/Pictures"},
  {"heic", DOWNLOADS_PATH + "/Pictures"},
  {"webp", DOWNLOADS_PATH + "/Pictures"},
  {"epub", DOWNLOADS_PATH + "/PDF_EPUB"},
  {"pdf", DOWNLOADS_PATH + "/PDF_EPUB"},
  {"docx", DOWNLOADS_PATH + "/Documents"},
  {"doc", DOWNLOADS_PATH + "/Documents"},
  {"apk", DOWNLOADS_PATH + "/APKs"},
  {"xapk", DOWNLOADS_PATH + "/APks"}
};

int main()
{
  fileArranger();
  terminalOutput();
  return 0;
}

// Function takes a string reference from the user and expands the user's home directory.
string expandUser(string &END_PATH)
{
  // get user's home directory
  const char* homeDirChar = getenv("HOME");

  if(homeDirChar == nullptr)
    {
      // in case the HOME environment variable is not set
      cerr << "Error: HOME environment variable is not set.\n";
      return "";
    }

  // combine home directory with the provided path
  string homeDir(homeDirChar);
  string expandedPath = homeDir + "/" + END_PATH;

  // return the home directory with the provided path
  return expandedPath;
}

void fileArranger()
{
  vector<string> extList;
  fs::path downloadPath(DOWNLOADS_PATH);

  if(!fs::exists(downloadPath) || !fs::is_directory(downloadPath))
    {
      cerr << "Error: Download path does not exist or is not a directory.\n";
      return;
    }

  fs::directory_iterator endIterator; // default constructor yields past-the-end
  for (fs::directory_iterator it(downloadPath); it != endIterator; ++it)
    {
      if (!fs::is_regular_file(it->status()))
	{
	  continue; // Skip non-regular files (directories, symlinks, etc.)
	}

      string file = it->path().filename().string();
      size_t dotPos = file.find_last_of('.');

      if (dotPos == string::npos)
	{
	  continue; // Skip files without an extension
	}

      string newExt = file.substr(dotPos + 1);
      if (FOLDER_EXT_PATHS.find(newExt) != FOLDER_EXT_PATHS.end())
	{
	  fs::path newPath(FOLDER_EXT_PATHS[newExt]);
	  if (!fs::exists(newPath))
	    {
	      fs::create_directories(newPath);
	    }
	}

      string ext = file.substr(dotPos + 1);
      /*
        Used to convert each character in the ext string to its lowercase
        equivalent.
        For example, if file is "Example.TXT", the std::transform call will
        convert ext to "txt".This is useful for case-insensitive comparisons
	when checking if the file extension is present in the FOLDER_EXT_PATHS map.
      //  std::transform(ext.begin(), ext.end(), ext.begin(), tolower);
      */

      if (FOLDER_EXT_PATHS.find(ext) != FOLDER_EXT_PATHS.end())
	{
	  fs::path path(FOLDER_EXT_PATHS[ext]);
	  if(fs::exists(path))
	    {
	      cout << path << "\n";
	    }

	  fs::path sourcePath = downloadPath / file;
	  fs::path destinationPath = fs::path(FOLDER_EXT_PATHS[ext]) / file;

	  fs::rename(sourcePath, destinationPath);
	}
    }
}

void terminalOutput()
{
  // init screen and sets up screen
  initscr();

  // print to screen
  printw("Your files are being sorted. Check your '~/Downloads' folder.");

  // refreshes the screen
  refresh();

  // pause the screen output
  getch();

  // deallocate memory and end ncurses
  endwin();
  return;
}
