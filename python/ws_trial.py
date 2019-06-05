domain = 'http://ctel.usm.maine.edu/cms150/content'
pages = ['course-schedule', 'syllabus', 'weeks-1-2-may-16-–-29', 'weeks-13-14-aug-8-21-and-finals-week-aug-22-26']

urls = []

for page in pages:
	url = domain + page
	urls.append(url)

print(urls)
