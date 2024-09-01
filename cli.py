import argparse
from data_processing import load_data, clean_data
from analysis import perform_analysis
from report import generate_report

def main():
    parser = argparse.ArgumentParser(description='AI for Data Analysis')
    parser.add_argument('file_path', type=str, help='Path to the data file')
    args = parser.parse_args()

    df = load_data(args.file_path)
    df = clean_data(df)
    analysis_results = perform_analysis(df)
    generate_report(df, analysis_results)

if __name__ == '__main__':
    main()
