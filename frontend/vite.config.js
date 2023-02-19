import { defineConfig } from 'vite';

export default defineConfig({
    base: "static/",
    build: {
        outDir: '../elimar/static/',
        manifest: true,
        rollupOptions: {
            input: './app.js',
        },
    },
});
