#!/usr/bin/env bash

# export TZ="America/New_York"
export TZ="UTC"

suite=${1:-example}
tag=$suite
if [[ "$suite" == "echo" ]] || [[ "$suite" == "example" ]]
then
    tag="master"
fi

outdir=${2:-reports}

while IFS=, read -r csid name ghid repo
do
    if [[ "$csid" == "csid" ]]
    then
        continue
    fi
    dt=`date +"%Y%m%d-%H%M%S"`
    dtz=`date +"%Z"`
    userdir="$outdir/$csid"
    mkdir -p $userdir
    outfile="$userdir/$csid-$suite-$dt"
    report="$outfile-report.txt"
    code="$outfile-code.tar.gz"

    echo "Downloading code: $code"
    curl -sLf -o $code "https://$GITHUBKEY@github.com/$ghid/$repo/archive/$tag.tar.gz"

    echo "Creating report: $report"
    echo "================================================================================" > $report
    echo "Assignment: $suite" >> $report
    echo "Student: $name <$csid@cs.odu.edu>" >> $report
    echo "Time: $dt $dtz" >> $report
    echo "Repository: https://github.com/$ghid/$repo/tree/$tag" >> $report
    echo "Server: cs531-$csid" >> $report
    echo "================================================================================" >> $report

    echo "" >> $report
    echo "Deploying server: cs531-$csid" | tee -a $report
    echo "" >> $report
    curl -s "http://cs531.cs.odu.edu/servers/deploy/$csid/$tag" >> $report
    echo "" >> $report

    sleep 5

    curl -Isf "http://cs531.cs.odu.edu/servers/logs/$csid" > /dev/null

    if [[ 0 -eq $? ]]
    then
        echo "" >> $report
        echo "Testing server: cs531-$csid against $suite test suite" | tee -a $report
        echo "" >> $report
        ./main.py "cs531-$csid" $suite >> $report

        echo "" >> $report
        echo "Destroying server: cs531-$csid" | tee -a $report
        curl -s "http://cs531.cs.odu.edu/servers/destroy/$csid" >> $report
        echo "" >> $report
    fi
done

echo "All done!"
