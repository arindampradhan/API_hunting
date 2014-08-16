Quick reference
You can view the following references to get an overview of creating the
following objects:
•	 BeautifulSoup
° ° soup = BeautifulSoup(string)
° ° soup = BeautifulSoup(string,features="xml")
° ° tag = soup.tag #accessing a tag
° °
° ° tag.name
•	 Tag
#Tag name
tag['attribute']
#Tag attribute


#for xmlChapter 2
•	 NavigableString
° °
soup.tag.string #get Tag's string



Quick reference
The following commands will help you to navigate down the tree:
•	 tag.name : This navigates to the child using the name
•	 tag.contents : This lists the children
•	 tag.children : This is a generator for children
•	 tag.descendants : This is a generator for descendants
•	 tag.string : This navigates to a string using .string
•	 tag.strings : This is a generator for strings
The following commands will help you to navigate up the tree:
•	 tag.parent : This navigates to the parent
•	 tag.parents : This is a generator for parents
The following commands will help you to navigate sideways:
•	 tag.next_sibling : This navigates to the next sibling
•	 tag.next_siblings : This is a generator for next siblings
•	 tag.previous_sibling : This navigates to the previous sibling
•	 tag.previous_siblings : This is a generator for previous siblings
The following commands help you to navigate to the previous or next element:
•	 tag.next_element : This navigates to the next element parsed
•	 tag.previous_element : This navigates to the previous element parsed


Quick reference
You can take a look at the following references to get an overview of the
modifying content:
•	 Modifying the Tag name:
The following code line modifies the name property:
° °
tag.name = "newvalue" : This line of code modifies the Tag
name as newvalue
•	 Modifying the Tag attribute:
The following code lines alter the attributes:
° °
° °
tag["attr"] = "newvalue" : This line of code modifies the Tag
attribute
del tag["attr"] : This line of code deletes the Tag attribute
•	 Adding new tags:
The following code lines correspond to the addition of content:
° ° newtag = soup.new_tag('tagname') : This line of code creates
newtag
° ° oldtag.append(newtag) : This line of code appends newtag to
oldtag.contents
° ° oldtag.insert(0,newtag) : This line of code inserts newtag at the
index 0 of oldtag.contents
[ 84 ]Chapter 5
•	 Modifying the string contents:
The following code lines are used to modify the string content:
° ° tag.string = "helloworld" : This line of code modifies tag.
string
° ° tag.append("helloworld") : This line of code appends
"helloworld" to the existing tag.string
° °
° °
newstring= soup.new_string("helloworld") : This line of code
creates a new NavigableString object
tag.insert(0,newstring) : This line of code inserts newstring at
the index 0 of tag.string
•	 Deleting the existing tags:
The following code lines help to remove the existing tag attributes:
° °
° °
° °
tag.decompose() : This line of code removes a tag and its children
tag.extract(): This line of code removes and returns a tag
or string
tag.clear() : This line of code removes children
•	 Special functions:
The following are the special functions used to add or alter tags:
° ° oldtag.insert_after(newtag) : This function inserts newtag after
oldtag
° ° oldtag.insert_before(newtag) : This function inserts newtag
before oldtag
° ° oldtag.replace_with(newtag) : This function replaces oldtag with
newtag
° ° oldtag.wrap(newtag) : This function wraps oldtag with newtag
° ° oldtag.unwrap(newtag) : This function unwraps newtag within
oldtag
