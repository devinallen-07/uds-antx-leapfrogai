import flowbitePlugin from 'flowbite/plugin';
import typography from '@tailwindcss/typography';
import colors from 'tailwindcss/colors';
import type { Config } from 'tailwindcss';

export default {
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		'./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'
	],

	theme: {
		fontWeight: {
			thin: '100',
			hairline: '100',
			extralight: '200',
			light: '300',
			normal: '300',
			semimedium: '400',
			medium: '500',
			semibold: '600',
			bold: '700',
			extrabold: '800',
			black: '900'
		},
		extend: {
			animation: {
				scrolling1: 'loop1 90s linear infinite',
				'scrolling1-fast': 'loop1 45s linear infinite',
				'scrolling2-fast': 'loop2 45s linear infinite',
				scrolling2: 'loop2 90s linear infinite',
				fade: 'fadeOut 4s forwards'
			},
			colors: {
				'du-white': '#e6e6e6',
				'du-dkGray': '#323336',
				'du-red': '#eb2126',
				'du-ltRed': '#eb6970',
				'du-dkRed': '#6e0000',
				'du-purple': '#9f00db',
				'du-ltPurple': '#b278d9',
				'du-dkPurple': '#411061',
				'du-ltBlue': '#2494d1',
				'du-dkBlue': '#102349',
				'du-blue': '#144A8F',
				'du-green': '#9ACC5B'
			},
			backgroundImage: {
				card: 'linear-gradient(145deg, #144A8F 84%, #19275B 70%, #1A1F4F 70%, #192456 70%, #172B5F 70%, #144A8F 80%)',
				button: 'linear-gradient(112deg, #6E0000 44.55%, #EB2126 98.7%)'
			},
			textColor: {
				DEFAULT: colors.white
			},
			fontFamily: {
				body: ['Poppins', 'arial', 'sans-serif'],
				header: ['Teko', 'arial', 'sans-serif'],
				code: ['monospace']
			}
		}
	},
	darkMode: 'class',

	plugins: [flowbitePlugin, typography]
} as Config;
