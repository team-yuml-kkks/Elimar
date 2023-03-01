import path from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
    base: "/static/",
    build: {
        outDir: '../elimar/static/',
        manifest: true,
        rollupOptions: {
            input: './app.js',
            output: {
                sourcemap: true,
                format: 'iife',
                name: 'app',
                assetFileNames: 'bundle.css',
                dir: '../elimar/static/',
                entryFileNames: 'app.js'
            }
        },
    },
    resolve: {
        alias: {
            '~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap'),
        }
    },
});
