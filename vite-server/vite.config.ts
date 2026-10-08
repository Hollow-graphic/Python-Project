import adapter from '@sveltejs/adapter-auto';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { cloudflare } from '@cloudflare/vite-plugin';

export default defineConfig({
	plugins: [
		sveltekit({
			compilerOptions: {
				runes: ({ filename }) =>
					filename.split(/[/\\]/).includes('node_modules')
						? undefined
						: true
			},
			adapter: adapter()
		}),

		cloudflare({
			tunnel: {
				name: 'hollow_miaou'
			}
		})
	],
	server: {
		allowedHosts: ['.trycloudflare.com']
	}
});