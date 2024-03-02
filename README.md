# Blender / R3F / Websockets Demo

Working demo of rendering text strings through Blender, compressing the resulting model and sending it to a Vite/R3F project to be displayed.  The whole thing is orechestrated via a simple websockets server. 

> NOTE : This was created for a project that required transcription be baked in, so if you want to skip the Whisper part entirely and just update the text files another way the project will still work fine.

Works with Blender 4.0.2 on MacOS.

## Installation

1. Run `npm install` in both the site and server folders.

2. Install [Whisper Stream](https://github.com/yohasebe/whisper-stream) on your system.

3. Update the `PATHS` object in [server/blenderToSite.js](/server/blenderToSite.js) to fit your system. (Paths must be absolute.)

## Initializing a Session

1. Start server :
```bash
cd server
node server.js
```

2. In a new terminal pane, start site : 
```bash
cd site
yarn dev # `npm run dev` should also work here if you aren't using yarn.
```

3. In a third terminal pane, begin transcription : 
```bash
whisper-stream -s 0.5 -p2 'tee -a /absolute/path/to/transcript.txt' # Internet required
```

**NOTE : Site will be blank until the first update to generator/text/transcription.txt.**

## Gotchyas

- Your blend files must be saved in **Object Mode**.



## Todo

- Get transcription running locally.
