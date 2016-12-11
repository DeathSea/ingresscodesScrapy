import sqlite3,os
db = sqlite3.connect("test.db")

c = db.cursor()

c.execute("""create table if not exists passcode (
	id INTEGER PRIMARY KEY autoincrement,
	passcode BLOB,
	title TEXT,
	source TEXT,
	filename TEXT,
	decode_method_tags TEXT
	)""")
c.execute("delete from passcode;")
c.execute("update sqlite_sequence set seq=1 where name=\"passcode\"")
content = None
with open('..'+os.sep+'code_post_map.txt','r') as f:
	content = f.read()
rows = []
if content is not None:
	k = False
	for line in content.splitlines():
		if not k:
			k = True
			continue#skip first line
		if line:
			row = []
			for col in line.split("\t"):
				row.append(col.strip().decode("u8"))
			rows.append(tuple(row))
print rows
c.executemany("insert into passcode values (NULL,?,?,?,?,?)",rows)
c.close()
db.commit()
db.close()