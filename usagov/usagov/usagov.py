import json
from collections import defaultdict

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort(reverse=True)
    return value_key_pairs[:n]
 
def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

def main():
    patch ='usagov_bitly_data2012-03-16-1331923249.txt'
    records = [json.loads(line) for line in open(patch)]
    print (records[0])
    print (records[0]['tz'])
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    print (time_zones[:10])

    counts = get_counts(time_zones)
    print ("counts tz: ", len(counts))
    print ("\nTop 10 counts:")

    topc = top_counts(counts)
    for x in topc:
        print(x[0], x[1])


if __name__ == '__main__':
    main()
