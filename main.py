#!/usr/bin/env python3
"""
Video Segment Downloader & Converter
Main entry point for the application
"""

import sys
import argparse
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from core.pipeline import VideoPipeline
from core.config import Config
from core.logger import Logger


def create_parser():
    """Create command-line argument parser"""
    parser = argparse.ArgumentParser(
        description='Download and merge video segments into MP4',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s -u "https://...og_{}.ts" -o video.mp4
  %(prog)s -u urls.txt -o video.mp4
  %(prog)s -u "https://...og_{}.ts" -o video.mp4 --keep-segments
        '''
    )
    
    parser.add_argument(
        '-u', '--url',
        required=True,
        help='URL template, list of URLs, or file path with URLs'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='output.mp4',
        help='Output video filename (default: output.mp4)'
    )
    
    parser.add_argument(
        '--download-dir',
        default='./video_segments',
        help='Directory for downloaded segments'
    )
    
    parser.add_argument(
        '--temp-dir',
        default='./video_temp',
        help='Temporary directory'
    )
    
    parser.add_argument(
        '--timeout',
        type=int,
        default=30,
        help='Download timeout in seconds (default: 30)'
    )
    
    parser.add_argument(
        '--keep-segments',
        action='store_true',
        help='Keep downloaded .ts files after merge'
    )
    
    parser.add_argument(
        '--keep-temp',
        action='store_true',
        help='Keep temporary files'
    )
    
    parser.add_argument(
        '--log-file',
        default='video_downloader.log',
        help='Log file path (default: video_downloader.log)'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode'
    )
    
    return parser


def main():
    """Main entry point"""
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        # Initialize logger
        logger = Logger(log_file=args.log_file, debug=args.debug)
        logger.info('='*70)
        logger.info('VIDEO DOWNLOADER & CONVERTER')
        logger.info('='*70)
        
        # Create config
        config = Config(
            download_dir=args.download_dir,
            temp_dir=args.temp_dir,
            output_video=args.output,
            timeout=args.timeout
        )
        
        logger.success(f'Configuration loaded')
        
        # Create and run pipeline
        pipeline = VideoPipeline(config, logger)
        
        success = pipeline.run(
            urls=args.url,
            output_video=args.output,
            keep_segments=args.keep_segments,
            keep_temp=args.keep_temp
        )
        
        logger.info('='*70)
        
        if success:
            logger.success('VIDEO PROCESSING COMPLETED SUCCESSFULLY')
            logger.info(f'Output: {args.output}')
            return 0
        else:
            logger.error('VIDEO PROCESSING FAILED')
            return 1
    
    except KeyboardInterrupt:
        logger.warning('Interrupted by user')
        return 130
    except Exception as e:
        logger.error(f'Fatal error: {str(e)}', exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
