# -*- coding: utf-8 -*-

from microdot import Microdot, send_file, Request

app = Microdot()
Request.max_content_length = 1024 * 1024  # 1MB (change as needed)

@app.get('/')
async def index(request):
    # return 'hello'
    return send_file('simple_uploads.html')

@app.post('/upload')
async def upload(request):
    # obtain the filename and size from request headers
    filename = request.headers['Content-Disposition'].split(
        'filename=')[1].strip('"')
    size = int(request.headers['Content-Length'])


    # sanitize the filename
    filename = filename.replace('/', '_')
    print('file_transfert_begin')
    print(filename)
    content = ''
    # write the file to the files directory in 1K chunks
    # with open('files/' + filename, 'wb') as f:
    while size > 0:
        chunk = await request.stream.read(min(size, 1024))
        # f.write(chunk)
        content += str(chunk)
        size -= len(chunk)
    print(content)
    print('file_transfert_end')
    return ''


if __name__ == '__main__':
    app.run(debug=True)
