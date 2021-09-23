import sys, os
import argparse
import networkx as nx

def build_cluster2header_dict(cdhit_infile):
    '''
    builds a cluster to header dictionary based off of cdhit clustering
    returns: header2cluster and cluster2header dictionary
    '''

    cluster2header_dict = dict()
    header2cluster_dict = dict()

    with open(cdhit_infile) as infile:
        for line in infile:
            line = line.rstrip('\n')
            # get cluster numer
            if line.startswith('>Cluster'):
                cluster_num = int(line.lstrip('>Cluster '))+1
            else:
                header = (line.split()[2].strip('...').strip('>')) 
                if cluster_num not in cluster2header_dict:
                    cluster2header_dict[cluster_num] = list()
                cluster2header_dict[cluster_num].append(header)
                header2cluster_dict[header]=cluster_num

    return(cluster2header_dict, header2cluster_dict)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Takes blast results and cdhit results and outputs network gml file; network: MGE to spacer network')
    parser.add_argument("-o", "--outfile", help = "output GML file path")
    parser.add_argument("--phage", help="phage blast results")
    parser.add_argument("--plasmid", help = "plasmid blast results")
    parser.add_argument("-c", "--cdhit", help="cdhit output")
    args = parser.parse_args()

    # empty networkx graph
    G = nx.Graph()

    # build cluster to header dictionary
    cluster2header_dict, header2cluster_dict = build_cluster2header_dict(args.cdhit) 

    # add node per cluster
    for cluster in cluster2header_dict:
        G.add_node(f'Spacer {cluster}', vtype='spacer')

    # add phage to network
    with open(args.phage) as phage:
        for line in phage:
            line = line.rstrip('\n')
            sline = line.split('\t')
            qseqid = sline[0]
            sseqid = sline[1]
            pident = sline[2]
            qstart = sline[7]
            qend   = sline[8]
            protospacer_start = sline[9]
            protospacer_end   = sline[10]       

            sseqid = sseqid.split('|')[0]

            G.add_node( sseqid , vtype='phage')
            G.add_edge(f'Spacer {header2cluster_dict[qseqid]}', sseqid)


    # add plasmid to network
    with open(args.plasmid) as plasmid:
        for line in plasmid:
            line = line.rstrip('\n')
            sline = line.split('\t')
            qseqid = sline[0]
            sseqid = sline[1]
            pident = sline[2]
            qstart = sline[7]
            qend   = sline[8]
            protospacer_start = sline[9]
            protospacer_end   = sline[10] 

            sseqid = sseqid.split('|')[0]

            G.add_node( sseqid , vtype='plasmid')
            G.add_edge(f'Spacer {header2cluster_dict[qseqid]}', sseqid)


    # export network as gml
    nx.write_gml(G, args.outfile)
