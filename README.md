# Blender / R3F / Websockets Demo

Working demo of rendering text strings through Blender, compressing the resulting model and sending it to a Vite/R3F project to be displayed.  The whole thing is orechestrated via a simple websockets server. 

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

## Gotchyas

- Your blend files must be saved in **Object Mode**.


## Debugging
- https://gltf-viewer.donmccurdy.com/


## Todo

- Get transcription running locally.
-  